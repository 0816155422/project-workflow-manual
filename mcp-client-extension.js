/**
 * HAP/AICC MCP HTTP client for the repository's Streamable HTTP endpoint.
 * Keep MCP_API_KEY in a trusted runtime; do not bundle it into a public client.
 */
class HapAiccMcpClient {
  constructor(endpointUrl, apiKey, options = {}) {
    if (typeof endpointUrl !== 'string' || !/^https?:\/\//i.test(endpointUrl)) {
      throw new TypeError('endpointUrl must be an absolute HTTP(S) URL ending in /mcp');
    }
    if (typeof apiKey !== 'string' || !apiKey) throw new TypeError('apiKey is required');
    this.endpointUrl = endpointUrl.replace(/\/$/, '');
    this.apiKey = apiKey;
    this.fetch = options.fetch || globalThis.fetch;
    if (typeof this.fetch !== 'function') throw new Error('A Fetch API implementation is required');
  }

  async callTool(name, args = {}) {
    const response = await this.fetch(this.endpointUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${this.apiKey}` },
      body: JSON.stringify({
        jsonrpc: '2.0', id: `req-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
        method: 'tools/call', params: { name, arguments: args }
      })
    });
    const text = await response.text();
    let data;
    try { data = text ? JSON.parse(text) : {}; }
    catch { throw new Error(`MCP returned a non-JSON response (HTTP ${response.status})`); }
    if (!response.ok) throw new Error(data.message || data.error?.message || `MCP HTTP error ${response.status}`);
    if (data.error) throw new Error(`JSON-RPC error ${data.error.code}: ${data.error.message}`);
    const result = data.result;
    if (result?.isError) throw new Error(result.content?.map(item => item.text || '').join('\n') || `Tool ${name} failed`);
    const content = result?.content;
    const textBlock = Array.isArray(content) ? content.find(item => item.type === 'text')?.text : undefined;
    if (typeof textBlock === 'string') {
      try { return JSON.parse(textBlock); } catch { return textBlock; }
    }
    return result;
  }

  async getRepositoryStatus() { return this.callTool('repository_status'); }
  async listFiles(prefix = '') { return this.callTool('list_files', { prefix }); }
  async readFile(path) { return this.callTool('read_file', { path }); }
  async writeFile(path, content, message) { return this.callTool('write_file', { path, content, message }); }
  async getAuditLogTail(lines = 20) { return this.callTool('audit_log_tail', { lines }); }

  async checkHealth() {
    const base = this.endpointUrl.replace(/\/mcp$/, '');
    const response = await this.fetch(`${base}/mcp/health`);
    if (!response.ok) throw new Error(`Health endpoint returned HTTP ${response.status}`);
    return response.json();
  }
}

if (typeof module !== 'undefined' && module.exports) module.exports = HapAiccMcpClient;
if (typeof globalThis !== 'undefined') globalThis.HapAiccMcpClient = HapAiccMcpClient;

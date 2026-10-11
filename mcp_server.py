"""MCP server for Social Brand Audit Engine."""
import sys
import json
from client import SocialBrandAuditEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "audit_brand_social_metrics",
                "description": "Evaluates brand social engagement rate and identifies growth gaps",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "profile_metrics": {"type": "object"}
                    },
                    "required": ["profile_metrics"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "audit_brand_social_metrics":
            metrics = params.get("arguments", {}).get("profile_metrics", {})
            res = SocialBrandAuditEngine.run_audit(metrics)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()

There's an Apache-style access log at /app/access.log. Parse it and write a JSON
summary report to /app/report.json.

The report must be a JSON object with exactly these three keys:
- total_requests: integer, the total number of request lines in the log.
- unique_ips: integer, the number of distinct client IP addresses that appear in the log.
- top_path: string, the request path (e.g. "/index.html") that is requested most often.

Success criteria:
1. /app/report.json exists and contains a valid JSON object.
2. total_requests equals the actual number of request lines in /app/access.log.
3. unique_ips equals the actual number of distinct client IPs in /app/access.log.
4. top_path equals the actual most-requested path in /app/access.log.

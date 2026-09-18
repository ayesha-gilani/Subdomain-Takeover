# Alert Triage Checklist — Possible Subdomain Takeover Exposure

## 1. Identify the Affected Asset

- Record the affected subdomain.
- Identify the parent domain.
- Check the asset inventory to determine the business owner.
- Determine whether the subdomain is active, retired, or unknown.

## 2. Validate DNS Configuration

Check:

- CNAME record
- CNAME target
- Recent DNS changes
- Whether the target belongs to an approved third-party provider

Document the current DNS configuration before making changes.

## 3. Validate the Provider Response

Check whether the third-party resource:

- Returns HTTP 404
- Returns "No such application"
- Returns "Unknown host"
- Returns another provider-specific unavailable-resource message

A provider error alone does not confirm a takeover.

## 4. Check for Legitimate Changes

Contact or check with:

- DNS/domain administrator
- DevOps/infrastructure team
- SEO/marketing owner

Determine whether the configuration change or service removal was authorized.

## 5. Check for Unauthorized Content

If the subdomain is serving unexpected content:

- Preserve relevant evidence.
- Record timestamps and affected hostname.
- Capture available DNS/HTTP information.
- Escalate according to the organization's incident-response procedure.

## 6. Determine Severity

Potential exposure without evidence of unauthorized control:
Medium priority.

Confirmed unauthorized hosting or unexpected content:
Escalate to the organization's higher-severity incident process.

## 7. Escalate

Notify the appropriate:

- SOC/security team
- DNS/domain administrator
- DevOps/infrastructure team
- SEO/marketing asset owner
- Client/security contact if client infrastructure is affected

## 8. Document the Investigation

Record:

- Alert timestamp
- Affected subdomain
- DNS records
- Provider
- HTTP response
- Investigation findings
- Actions taken
- People/teams notified
- Final disposition
# Incident Response Playbook
## Possible Subdomain Takeover Exposure

### 1. Purpose

This playbook provides a standardized SOC response process for
investigating and responding to possible subdomain takeover exposure
within an SEO organization.

The objective is to identify potentially vulnerable or misconfigured
subdomains, validate the alert, contain confirmed exposure, and restore
the affected service safely.

---

## 2. Scope

This playbook applies to:

- Organization-owned domains and subdomains
- DNS records managed by the organization
- Third-party hosting and SaaS services
- SEO campaign and marketing subdomains
- Client-owned domains where the organization is responsible for
  DNS or web infrastructure

All investigation and testing must be performed only on authorized
systems.

---

## 3. Detection Trigger

The playbook is initiated when the SOC receives an alert containing
indicators such as:

- A subdomain using an external CNAME
- A third-party resource that appears unavailable
- HTTP 404 or provider-specific resource-not-found messages
- Unknown-host or missing-application responses
- Unexpected DNS changes
- Unexpected content appearing on an organization-owned subdomain

A detection alert is an indicator for investigation and does not
automatically confirm a successful takeover.

---

## 4. Initial Triage

The SOC analyst should:

1. Identify the affected subdomain.
2. Record the alert timestamp.
3. Review the DNS record and CNAME target.
4. Identify the third-party provider.
5. Check the provider response.
6. Review the organization's asset inventory.
7. Determine the business owner of the subdomain.
8. Check whether the configuration change was authorized.
9. Check for unexpected content or behavior.
10. Preserve relevant evidence.

---

## 5. Validation

The analyst should determine whether:

- The subdomain is still required.
- The third-party service is intentionally configured.
- The referenced resource still exists.
- The DNS record is stale or misconfigured.
- The provider response indicates an unavailable resource.
- Unauthorized content or control is present.

The alert should be closed as a false positive when the
configuration is verified as legitimate and functioning normally.

---

## 6. Containment

If exposure is confirmed or unauthorized control is suspected:

### If the subdomain is no longer required

Remove the stale DNS record through the organization's approved
DNS-management process.

### If the subdomain is still required

Restore or recreate the legitimate third-party resource and update
the DNS configuration if necessary.

### If unauthorized content is present

Restrict access or remove the affected DNS configuration through
authorized administrative procedures while preserving relevant
evidence.

Do not make unapproved DNS changes during investigation.

---

## 7. Notification and Escalation

Notify the relevant teams according to organizational procedures:

- SOC/security team
- DNS/domain administrator
- DevOps/infrastructure team
- SEO or marketing asset owner
- Client security/contact team when client infrastructure is affected

Escalate the incident when unauthorized content, unauthorized
control, or significant business impact is identified.

---

## 8. Remediation

After containment:

1. Remove unnecessary or stale DNS records.
2. Restore required legitimate services.
3. Verify DNS configuration.
4. Verify that the intended website/service is functioning.
5. Review related subdomains for similar configuration issues.
6. Update the asset inventory.
7. Record the responsible owner for each external service.
8. Review third-party service decommissioning procedures.

---

## 9. Recovery

After remediation:

- Verify expected DNS resolution.
- Verify the intended HTTP response.
- Confirm that unauthorized content is no longer accessible.
- Monitor the affected subdomain for abnormal activity.
- Confirm service availability with the responsible team.

The incident can be closed after the affected service has been
validated and monitoring shows no continuing suspicious activity.

---

## 10. Evidence to Preserve

Where available, preserve:

- DNS records
- DNS change history
- HTTP response information
- SIEM alert
- Relevant timestamps
- Provider error messages
- Asset ownership information
- Screenshots or other approved evidence
- Actions taken during response

Evidence should be stored according to the organization's
incident-response and retention procedures.

---

## 11. False Positive Handling

Potential false positives include:

- Temporary third-party service outages
- Planned application migrations
- DNS changes that were authorized
- Incorrect asset inventory information
- Temporary provider-side errors

Before closing the alert, the analyst should verify the configuration
with the responsible owner or approved change records.

---

## 12. Post-Incident Actions

After resolving the incident:

- Document the root cause.
- Update the asset inventory.
- Review similar DNS records.
- Improve monitoring coverage where necessary.
- Update the detection rule if new indicators were identified.
- Review third-party service decommissioning procedures.
- Record lessons learned.

---

## 13. Success Criteria

The incident is considered resolved when:

- The affected DNS configuration has been validated or corrected.
- Any unauthorized exposure has been contained.
- The intended service is functioning normally.
- Relevant stakeholders have been notified.
- Evidence and actions have been documented.
- Follow-up monitoring is in place.

---

## 14. Analyst Reminder

A possible subdomain takeover alert is an investigation trigger,
not proof of compromise.

Always validate:

DNS configuration → Provider status → Asset ownership →
Authorization → Unexpected content → Business impact
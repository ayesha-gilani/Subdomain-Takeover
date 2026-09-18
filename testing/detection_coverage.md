# Detection Coverage and Known Blind Spots

## Detection Coverage

The current detection logic is designed to identify log patterns
consistent with possible subdomain takeover exposure.

It looks for the combination of:

1. A DNS CNAME record.
2. An external/third-party provider.
3. An unavailable-resource indicator such as HTTP 404 or
   "No such application".

### Covered Scenario

The rule successfully detects the simulated scenario where an
organization-owned subdomain points to an unavailable third-party
resource.

### Tested Scenarios

| Scenario | Expected Result | Test Result |
|---|---|---|
| External CNAME + unavailable resource | Alert | PASS |
| External CNAME + successful HTTP response | No Alert | PASS |

## Known Blind Spots

The detection logic has several limitations:

### 1. Provider-specific responses

Different hosting providers may use different error messages.
The current pattern may not detect every provider.

### 2. Missing DNS logs

If DNS records or DNS change history are unavailable, the SOC may
not have enough information to validate the alert.

### 3. Missing HTTP telemetry

Some subdomains may not have accessible HTTP logs, reducing the
ability to correlate DNS and web activity.

### 4. Temporary service outages

A legitimate third-party outage may produce an error similar to a
dangling resource and create a false positive.

### 5. Legitimate configuration changes

Planned migrations or application changes may temporarily produce
similar indicators.

### 6. Detection is not proof of takeover

The rule identifies suspicious conditions. It does not prove that
an attacker has successfully claimed or controlled the resource.

Additional validation is required.

## Future Improvements

Future versions could include:

- A maintained inventory of organization-owned subdomains.
- Monitoring of DNS record changes.
- Provider-specific detection patterns.
- Automated DNS and HTTP correlation.
- Integration with a production SIEM.
- Alert enrichment with asset ownership information.
- Automated monitoring of unused or retired subdomains.
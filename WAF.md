
```mermaid
flowchart TD
    A[WAF] -->|Secure Data| B(Load  Balancer)
    B --> C{VPN Peering}
    C -->|Lightsail| D[Magento 2]


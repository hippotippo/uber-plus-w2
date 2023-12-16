```mermaid
graph LR
    subgraph AWS Cloud
        Lightsail[Magento on AWS Lightsail]
        LB[Load Balancer]
        ACM[AWS Certificate Manager]
        WAF[Web Application Firewall]
        R53[Route 53]
        VPN[VPN Peering]

        Lightsail -->|Traffic| LB
        LB -->|SSL/TLS| ACM
        LB -->|Secured Traffic| WAF
        WAF -->|Filtered Traffic| Lightsail
        Lightsail -->|VPN Connection| VPN
        VPN -->|VPN Connection| LB
        R53 -->|DNS Management| LB
    end

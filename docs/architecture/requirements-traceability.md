# Requirements Traceability Matrix

**Status:** Accepted baseline  
**Version:** 1.0

| Product requirement | Owning architecture | Primary proof |
|---|---|---|
| see every observed asset | Identity Resolver + Security Graph | Universe projection |
| know what communicates | Telemetry + Graph | Flow/relationship evidence |
| know what changed | temporal graph + detection | delta query/replay |
| inspect packet evidence | Evidence + SessionProvider | PCAP/session drill-down |
| distinguish alerts from conclusions | Detection/Correlation | Alert vs Finding model |
| explain why something matters | Investigation + Elyandra | evidence-backed hypothesis |
| act safely | Plays + Policy + Execution | grant/audit chain |
| continuous what-if response | Automation Engine | simulation/replay |
| local operation without cloud | Deployment | offline qualification |
| no vendor lock-in | Sovereignty Program | adapter/exit tests |
| wireless awareness | Network/Wireless | coverage + AP/client observations |
| protect separate zones | Network model + Policy | zone/scope rules |
| see Ely's own behavior | Operations + Audit | trace/ledger |
| recover history | Evidence + temporal graph | deterministic replay |
| future multiple sites/users | Workspace/Site + RBAC | tenant/site contracts |
| model cannot self-authorize | Policy boundary | security tests |

## Rule

A new product promise must acquire an owning architecture component and acceptance proof before implementation is considered complete.

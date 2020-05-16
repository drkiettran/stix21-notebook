# All about STIX 2.1

Python implementation/experiments of STIX 2.1

```python
# A total of 18 STIX Domain Object or SDOs
from stix2.v21 import (AttackPattern, Campaign, CourseOfAction, Grouping,
                       Identity, Indicator, Infrastructure, IntrusionSet,
                       Location, Malware, MalwareAnalysis, Note, ObservedData,
                       Opinion, Report, ThreatActor, Tool, Vulnerability)

# A total of 2 STIX Relationship Objects or SROs
from stix2.v21 import (Relationship, Sighting)

# a total of 18 STIX Cyber-observable Objects or SCOs
from stix2.v21 import (Artifact, AutonomousSystem, Directory, DomainName,
                       EmailAddress, EmailMessage, File, IPv4Address,
                       IPv6Address, MACAddress, Mutex, NetworkTraffic,
                       Process, Software, URL, UserAccount,
                       WindowsRegistryKey, X509Certificate)

# a total of 2 Meta Object or SMOs
from stix2.v21 import (LanguageContent, MarkingDefinition)

# a total of 1 STIX Bundle Object or SBO
from stix2.v21 import (Bundle)

# a total of 2 common data types.
from stix2.v21 import(ExternalReference, KillChainPhase)

```

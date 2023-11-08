## About the connector
Shadow server provides you with access to the most timely, critical Internet security like data collection,network reporting,investigation support ,reveal security vulnerabilities, expose malicious activity and help remediate victims.
<p>This document provides information about the Shadow Server Connector, which facilitates automated interactions, with a Shadow Server server using FortiSOAR&trade; playbooks. Add the Shadow Server Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Shadow Server.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-shadowserver`

## Prerequisites to configuring the connector
- You must have the URL of Shadow Server server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Shadow Server server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Shadow Server</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td><br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Origin Query<br></td><td>Report back the originating ASN and ASN name for the specific CIDR.<br></td><td>get_origin_query <br/>Investigation<br></td></tr>
<tr><td>Get Peer Query<br></td><td>Report back all the BGP peers for a specific CIDR.<br></td><td>get_peer_query <br/>Investigation<br></td></tr>
<tr><td>Get Prefix Query<br></td><td>Given an ASN report back all the routed CIDR's.<br></td><td>get_prefix_query <br/>Investigation<br></td></tr>
<tr><td>Get ASN Query<br></td><td>Report back any information about the ASN.<br></td><td>get_asn_query <br/>Investigation<br></td></tr>
<tr><td>Get Malware Query<br></td><td>Returns a JSON response containing static details about the requested sample as well as antivirus vendor and signature details.<br></td><td>get_malware_query <br/>Investigation<br></td></tr>
<tr><td>Get Programs Query<br></td><td>Returns a JSON response containing the details for the requested program. Replaces bin-test.shadowserver.org.<br></td><td>get_programs_query <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get Origin Query
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>IP Address<br></td><td>Specify the IP address.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asname_short": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "prefix": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asname_long": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "geo": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "nic": ""
</code><code><br>}</code>

### operation: Get Peer Query
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>IP Address<br></td><td>Specify the IP address<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "prefix": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "peer": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asname_short": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asname_long": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "geo": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "nic": ""
</code><code><br>}</code>

### operation: Get Prefix Query
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Query<br></td><td>Specify the Query.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get ASN Query
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Query<br></td><td>Specify the query.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asname_short": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "date": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asn": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "asname_long": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "geo": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "nic": ""
</code><code><br>}</code>

### operation: Get Malware Query
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>MD5<br></td><td>Specify the query<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "timestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "first_seen": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "sha1": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "anti_virus": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "md5": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "vendor": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "signature": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "timestamp": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "signature": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "timestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "md5": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "vendor": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "timestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "signature": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "vendor": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "md5": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "vendor": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "md5": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "timestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "signature": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "md5": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "vendor": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "timestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "signature": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "md5": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "vendor": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "timestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "signature": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "last_seen": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "sha256": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "md5": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "tlsh": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "import_hash": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "entropic": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "pehash": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "filesize": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "adobe_malware_classifier": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "sha512": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "magic": ""
</code><code><br>}</code>

### operation: Get Programs Query
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Query<br></td><td>Specify the query<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "product_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "sha512": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "os_version": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "fileversion": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "crc32": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "trusted_signature": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "binary": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "sig_trustfile": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "os_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "language": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "filename": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "reference": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "product_version": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "mfg_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "dirname": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "os_mfg": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "application_type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "filesize": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "signer": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "sig_timestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "filetimestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "strongname_signed": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "source_version": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "bit": ""
</code><code><br>}</code>
## Included playbooks
The `Sample - shadowserver - 1.0.0` playbook collection comes bundled with the Shadow Server connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Shadow Server connector.

- Get Origin Query
- Get Peer Query
- Get Prefix Query
- Get ASN Query
- Get Malware Query
- Get Programs Query

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.

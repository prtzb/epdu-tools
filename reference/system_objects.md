| XML Object Name | Access Right | Type | Description | Access | Default Value | Reboot Needed |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| System.Bootloader.iVersion | admin | String:15 |  | RO |  | False |
| System.Bootloader.Mode | superadmin | BootMode | Normal , Upgrade , Passthru , ATE , Bootstrap | RW | 0 | False |
| System.Contact | admin | String:31 |  | RW |  | False |
| System.DaisyChain.Count | admin | Integer0to65535 |  | RO | 3 | False |
| System.DaisyChain.DeviceId | admin | DaisyChainDeviceId | Host , Device 1 , Device 2 , Device 3 | RW | 1 | False |
| System.DaisyChain.Position | admin | DaisyChainPosition | Middle , End | RW | 0 | False |
| System.DaisyChain.Statistic | admin | String:127 |  | RO |  | False |
| System.DaisyChain.Status | admin | DaisyChainStatus | No Communication , Communication OK , Communication failed , Host conflict , Device conflict | RO | 0 | False |
| System.DaisyChain[x].DeviceId | admin | DaisyChainDeviceId | Host , Device 1 , Device 2 , Device 3 | RO | 1 | False |
| System.DaisyChain[x].MacAddress | admin | String:17 |  | RO | 00:00:00:00:00:00 | False |
| System.DaisyChain[x].Position | admin | DaisyChainPosition | Middle , End | RO | 0 | False |
| System.DaisyChain[x].Status | admin | DaisyChainStatus | No Communication , Communication OK , Communication failed , Host conflict(not implemented) , Device conflict | RO | 0 | False |
| System.Display.Contrast | admin | Integer25to45 |  | RW | 32 | False |
| System.Display.Language | superadmin | DisplayLanguage | English , French , German , Spanish , Russian , Portuguese , Italian | RW | 0 | False |
| System.Display.LcdRotation | admin | LcdRotation | Rotation 0 Deg(0U) , Rotation 90 Deg(1U) , Rotation 180 Deg(0U) , Rotation 270 Deg(1U) | RW | 0 | False |
| System.Display.Password | superadmin | Password:4 |  | RW | 1234 | False |
| System.Display.Password.IsEnable | superadmin | ControlState |  | RW | 0 | False |
| System.EepromBackup.Reset | superadmin | ControlState |  | WO | 0 | False |
| System.Email.Count | admin | Integer0to65535 |  | RO | 9 | False |
| System.Email.Sender | admin | String:31 |  | RW | PDU@Eaton.com | False |
| System.Email[x].Description | admin | String:63 |  | RW | , , ,  | False |
| System.Email[x].EventList.All | admin | EventType |  | RW | 0 | False |
| System.Email[x].Events.Log | admin | ControlState |  | RW | 0 | False |
| System.Email[x].Recipient | admin | String:127 |  | RW | email1@recipient.com, email2@recipient.com, email3@recipient.com, email4@recipient.com, email5@recipient.com, email6@recipient.com, email7@recipient.com, email8@recipient.com, email9@recipient.com | False |
| System.Email[x].Report.Hour | admin | Time0to23hours |  | RW | 0 | False |
| System.Email[x].Report.Next | admin | Time0to31days |  | RW | 0 | False |
| System.Email[x].Report.Periodicity | admin | Time0to28days |  | RW | 0 | False |
| System.Email[x].Selected | admin | ControlState | Disabled , Enabled | RW | 0 | False |
| System.Email[x].Test | admin | Boolean |  | WO | 0 | False |
| System.Ethernet.iSerialNumber | admin | String:31 |  | RO |  | False |
| System.Ethernet.iVersion | admin | String:15 |  | RO | 01.00.0031 | False |
| System.Ethernet.MacAddress | admin | String:31 |  | RO | 00:00:00:00:00:00 | False |
| System.Ethernet.Mode | admin | EthMode | Auto Negotiation , 100 Mbps Full Duplex , 100 Mbps Half Duplex , 10 Mbps Full Duplex , 10 Mbps Half Duplex | RW | 0 | True |
| System.FactoryReset | admin | Boolean |  | WO | 0 | False |
| System.FirmwareUpgrade | admin | Boolean |  | RW | 1 | False |
| System.FirmwareUpgradeMode | admin | ControlState |  | WO | 0 | False |
| System.FormatFS | superadmin | ControlState |  | WO | 0 | False |
| System.KeepDC | admin | ControlState |  | RW | 0 | False |
| System.KeepIP | admin | ControlState |  | RW | 0 | False |
| System.Language | admin | Language | English(ENG) , French(FRE) , Spanish(SPA) , German(GER) , Italian(ITA) , Chinese Simplified(CHI) , Japanase(JPN) , Korean(KOR) 10, Chinese Traditionnal(CHT) 11, Russian(RUS) 12, Portuguese(POR) 13, Czech(CZE) 14, Polish(POL) | RW | 2 | False |
| System.Location | admin | String:31 |  | RW |  | False |
| System.Login | superadmin | String:31 |  | RW | admin | False |
| System.LogReset | admin | Boolean |  | WO | 0 | False |
| System.Network.Authentication.AuthMethod | admin | AuthMethod | Local Authentication , LDAP Authentication , Radius Authentication | RW | 1 | False |
| System.Network.Authentication.AuthOrder | admin | AuthOrder | Local , External then Local , Local then External , External | RW | 1 | False |
| System.Network.Authentication.MaxSessionTime | admin | Integer0to42949672 |  | RW | 1800 | False |
| System.Network.Authentication.SessionTime | admin | Integer0to42949672 |  | RW | 300 | False |
| System.Network.DHCP | admin | ControlState |  | RW | 1 | True |
| System.Network.DomainName | admin | String:63 |  | RW | pdu.domain.com | True |
| System.Network.EnergyWise.Cmd | admin | EnergyWiseCmd | Start , Stop , Restart | WO | 0 | False |
| System.Network.EnergyWise.Domain | admin | String:63 |  | RW | MyDomain | False |
| System.Network.EnergyWise.Enable | admin | ControlState | isable , nable | RW | 0 | False |
| System.Network.EnergyWise.ListenPort | admin | Integer1to65535 |  | RW | 48296 | False |
| System.Network.EnergyWise.RemotePort | admin | Integer1to65535 |  | RW | 43440 | False |
| System.Network.EnergyWise.SdkVersion | admin | String:31 |  | RO | RELEASE1.2.0 | False |
| System.Network.EnergyWise.Secret | admin | ControlState |  | RW | 0 | False |
| System.Network.EnergyWise.SecretKey | admin | Password:63 |  | RW |  | False |
| System.Network.EnergyWise.SeqId | admin | Integer0to42949672 |  | RW | 0 | False |
| System.Network.EnergyWise.State | admin | String:31 |  | RO |  | False |
| System.Network.EnergyWise.ThresholdLevel | admin | Integer0to10 |  | RW | 4 | False |
| System.Network.FTP.Access | admin | ControlState |  | RW | 1 | True |
| System.Network.HostName | admin | String:31 |  | WO | ePDU$x | True |
| System.Network.HTTP.Access | admin | ControlState |  | RW | 1 | True |
| System.Network.HTTP.Port | admin | Integer1to65535 |  | RW | 80 | True |
| System.Network.HTTPS.KeySize | admin | SslKeySize | 1024 bits , 2048 bits | RW | 0 | True |
| System.Network.HTTPS.Port | admin | Integer1to65535 |  | RW | 443 | True |
| System.Network.IPAddress | admin | IPv4 |  | WO | 192.168.123.123 | True |
| System.Network.IPGateway | admin | IPv4 |  | RW |  | True |
| System.Network.IPMask | admin | IPv4 |  | RW | 255.255.0.0 | True |
| System.Network.IPv6Address1 | admin | IPv6 |  | WO |  | True |
| System.Network.IPv6Address2 | admin | IPv6 |  | RO |  | False |
| System.Network.IPv6AutoConfig | admin | ControlState |  | RW | 0 | True |
| System.Network.IPv6DefaultGateway | admin | IPv6 |  | RW |  | True |
| System.Network.IPv6Enable | admin | ControlState |  | RW | 0 | True |
| System.Network.IPv6LocalAddress | admin | IPv6 |  | RO |  | False |
| System.Network.IPv6Status | admin | NetworkIpv6Status | Invalid , Valid , Manual Configuration | RO | 0 | False |
| System.Network.Ldap.AuthMechanism | admin | LdapAuthMechanis | imple , Digest MD5 | RW | 0 | False |
| System.Network.Ldap.CheckServerCertificat | admin | ControlState |  | RW | 0 | False |
| System.Network.Ldap.GroupSearch.AuthzMode | admin | LdapAuthorizationM | No Authz , By User Attribut , By Group | RW | 0 | False |
| System.Network.Ldap.GroupSearch.BaseDn | admin | String:249 |  | RW |  | False |
| System.Network.Ldap.GroupSearch.UPSGroupNameAttr | admin | String:49 |  | RW |  | False |
| System.Network.Ldap.GroupSearch.UserNameAttr | admin | String:49 |  | RW |  | False |
| System.Network.Ldap.SearchMode | admin | LdapSearchMode | Anonymous Search , User Bind Search | RW | 0 | False |
| System.Network.Ldap.SearchUser | admin | String:249 |  | RW |  | False |
| System.Network.Ldap.SearchUserPassword | admin | Password:49 |  | RW |  | False |
| System.Network.Ldap.Server.Count | admin | Integer0to10 |  | RO | 2 | False |
| System.Network.Ldap.Server[x].IsEnable | admin | ControlState |  | RW | 0 | False |
| System.Network.Ldap.Server[x].Port | admin | Integer1to65535 |  | RW | 389 | False |
| System.Network.Ldap.Server[x].ServerName | admin | String:49 |  | RW | LDAPServer1, LDAPServer2 | False |
| System.Network.Ldap.Server[x].TimeOut | admin | Integer0to65535 |  | RW | 10 | False |
| System.Network.Ldap.ServerType | admin | LdapServerType | Generic LDAP server , Active Directory | RW | 0 | False |
| System.Network.Ldap.SSLMode | admin | LdapSSLMode | o SSL , SSL (LDAPS) , SSL (Start TLS) | RW | 0 | False |
| System.Network.Ldap.UserSearch.Attribute | admin | String:49 |  | RW |  | False |
| System.Network.Ldap.UserSearch.BaseDn | admin | String:249 |  | RW |  | False |
| System.Network.Ldap.UserSearch.Object | admin | String:49 |  | RW |  | False |
| System.Network.PrefixLength1 | admin | Integer0to128 |  | RW | 0 | True |
| System.Network.PrefixLength2 | admin | Integer0to128 |  | RO | 0 | False |
| System.Network.PrimaryDNS | admin | IPv4 |  | RW |  | True |
| System.Network.Radius.AuthType | admin | RadiusAuthType | PAP , CHAP | RW | 0 | False |
| System.Network.Radius.Server.Count | admin | Integer0to10 |  | RO | 2 | False |
| System.Network.Radius.Server[x].IsEnable | admin | ControlState |  | RW | 0 | False |
| System.Network.Radius.Server[x].NasIdentiferType | admin | NasIdentifierType | IDENTIFER_IPV4 , IDENTIFER_IPV6_1 , IDENTIFER_IPV6_2 , IDENTIFER_IPV6_LOCAL | RW | 0 | False |
| System.Network.Radius.Server[x].Port | admin | Integer1to65535 |  | RW | 1812 | False |
| System.Network.Radius.Server[x].Retry | admin | Integer0to255 |  | RW | 3 | False |
| System.Network.Radius.Server[x].ServerName | admin | String:48 |  | RW | RADIUSServer1, RADIUSServer2 | False |
| System.Network.Radius.Server[x].SharedSecret | admin | Password:48 |  | RW |  | False |
| System.Network.Radius.Server[x].Timeout | admin | Integer1to65535 |  | RW | 5 | False |
| System.Network.SecondaryDNS | admin | IPv4 |  | RW |  | True |
| System.Network.SmtpServer.Authentication | admin | ControlState |  | RW | 0 | False |
| System.Network.SmtpServer.HostName | admin | String:63 |  | RW |  | False |
| System.Network.SmtpServer.Login | admin | String:31 |  | RW |  | False |
| System.Network.SmtpServer.Password | admin | Password:31 |  | RW |  | False |
| System.Network.SmtpServer.Port | admin | Integer1to65535 |  | RW | 25 | False |
| System.Network.SNMP.Port | admin | Integer1to65535 |  | RW | 161 | False |
| System.Network.SNMP.snmpVersion | admin | SNMPVersion | disabled , SNMP V1 , SNMP V3 , SNMP V1&V3 | RW | 0 | False |
| System.Network.SNMP.TrapPort | admin | Integer1to65535 |  | RW | 162 | False |
| System.Network.SNMP.V1.User.Count | admin | Integer0to65535 |  | RO | SNMPV1_NBCOMMUNITIES | False |
| System.Network.SNMP.V1.User[x].SecurityRight | admin | Snmpv3VacmSecurit | No Access , Read-Only , Read/Write | RW | 0 | False |
| System.Network.SNMP.V1.User[x].UserName | admin | String:24 |  | RW | public, private | False |
| System.Network.SNMP.V3.User.Count | admin | Integer0to65535 |  | RO | SNMPV3_USM_NBUSERS | False |
| System.Network.SNMP.V3.User[x].Name | admin | String:31 |  | RW | SNMPv3User1, SNMPv3User2, SNMPv3User3, SNMPv3User4 | False |
| System.Network.SNMP.V3.User[x].Password | admin | Password:24 |  | RW | ,  | False |
| System.Network.SNMP.V3.User[x].PrivacyKey | admin | Password:24 |  | RW | ,  | False |
| System.Network.SNMP.V3.User[x].SecurityLevel | admin | Snmpv3UsmLevel | Not Set , No Auth No Priv , Auth No Priv , Auth Priv | RW | 0 | False |
| System.Network.SNMP.V3.User[x].SecurityRight | admin | Snmpv3VacmSecurit | No Access , Read-Only , Read/Write | RW | 0 | False |
| System.Network.SSH.Port | admin | Integer1to65535 |  | RW | 22 | True |
| System.Network.Syslog.Server.Count | admin | Integer0to10 |  | RO | 2 | False |
| System.Network.Syslog.Server[x].BOM | admin | ControlState |  | RW | 1 | False |
| System.Network.Syslog.Server[x].Facility | admin | SyslogFacility | kernel messages , user-level messages , mail system , system daemons , security/authorization messages , messages generated internally by syslogd , line printer subsystem , network news subsystem , UUCP subsystem , clock daemon 1, security/authorization messages 1, FTP daemon 1, NTP subsystem 1, log audit 1, log alert 1, clock daemon (note 2) 1, local use 0 (local0) 1, local use 1 (local1) 1, local use 2 (local2) 1, local use 3 (local3) 2, local use 4 (local4) 2, local use 5 (local5) 2, local use 6 (local6) 2, local use 7 (local7) | RW | 1 | False |
| System.Network.Syslog.Server[x].IsEnable | admin | ControlState |  | RW | 0 | False |
| System.Network.Syslog.Server[x].MessageTransfer | admin | SyslogMessageTran | Octet Counting , Non Transparent Framing | RW | 0 | False |
| System.Network.Syslog.Server[x].Port | admin | Integer1to65535 |  | RW | 514 | False |
| System.Network.Syslog.Server[x].Protocol | admin | SyslogProtocol | UDP , TCP | RW | 0 | False |
| System.Network.Syslog.Server[x].ServerName | admin | String:49 |  | RW | SyslogServer1, SyslogServer2 | False |
| System.Network.Syslog.Server[x].Test | admin | Boolean |  | WO | 0 | False |
| System.Network.Telnet.Access | admin | ControlState |  | RW | 1 | True |
| System.Network.Telnet.Port | admin | Integer1to65535 |  | RW | 23 | True |
| System.Network.Telnet.Security | admin | ControlState |  | RW | 0 | True |
| System.NetworkManagementSystem.Count | pdu | Integer0to65535 |  | RO | NB_TRAP_RECEIVERS | False |
| System.NetworkManagementSystem[x].EventList.All | pdu | EventType | None , All Alarms | RW | 0 | False |
| System.NetworkManagementSystem[x].HostName | pdu | String:63 |  | RW | , , ,  | False |
| System.NetworkManagementSystem[x].Name | pdu | String:31 |  | RW | TrapReceiver1, TrapReceiver2, TrapReceiver3, TrapReceiver4, TrapReceiver5, TrapReceiver6, TrapReceiver7, TrapReceiver8 | False |
| System.NetworkManagementSystem[x].Test | pdu | Boolean |  | WO | 0 | False |
| System.NetworkManagementSystem[x].TrapCommunity | pdu | String:24 |  | RW | public, public, public, public, public, public, public, public | False |
| System.NetworkManagementSystem[x].TrapSnmpVersion | pdu | TrapSNMPVersion | Disabled , SNMP V1 , SNMP V3 | RW | 0 | False |
| System.Password | superadmin | Password:15 |  | RW | admin | False |
| System.Restart | admin | Boolean |  | WO | 0 | False |
| System.Security | admin | ControlState |  | RW | 0 | True |
| System.Slip.Statistic | admin | String:31 |  | RO |  | False |
| System.Temperature.Unit | admin | TemperatureUnit | °C , °F | RW | 1 | False |
| System.Time | admin | Time0to136years |  | RW | 0 | False |
| System.TimeDaylight | admin | ControlState |  | RW | 0 | False |
| System.TimeFormat | admin | DateTimeFormat | mm/dd/yyyy , dd/mm/yyyy , yyyy-mm-dd , dd mm yyyy | RW | 2 | False |
| System.TimeNtp | admin | String:63 |  | RW |  | False |
| System.TimeSync | admin | DateTimeSource | Manual , Sync NTP | RW | 0 | False |
| System.TimeUp | admin | Time0to136years |  | RO | 0 | False |
| System.TimeZone | admin | DateTimeTimeZone | 43200, -39600, -36000, -32400, -28800, -25200, -21600, -18000, -16200, -14400, -12600, -10800, -7200, - 3600, 0, 3600, 7200, 10800, 12600, 14400, 16200, 18000, 19800, 21600, 23400, 25200, 28800, 32400, 34200, 36000,  39600, 43200 | RW | 0 | False |
| System.User.Count | admin | Integer0to65535 |  | RO | 8 | False |
| System.User[x].Login | admin | String:31 |  | RW | Account1, Account2, Account3, Account4, Account5, Account6, Account7, Account8 | False |
| System.User[x].Password | admin | Password:15 |  | RW | , , ,  | False |
| System.User[x].Profile | admin | MultiUserProfile | superadmin , admin , ePDU User , Outlet User | RW | 0 | False |
| System.User[x].SecurityRight | admin | MultiUserAccess | No Access , Read-Only , Read/Write | RW | 0 | False |
| System.User[x].Status | admin | ControlState |  | RW | 0 | False |
| System.User[x].Type | admin | MultiUserType | local , remote | RW | 0 | False |
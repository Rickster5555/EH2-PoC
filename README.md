# Cacti Unauthenticated Command Injection (CVE-2022-46169)
This is a simple PoC adaptation of the Vulnhub's Cacti scenario. You can check it out [here](https://github.com/vulhub/vulhub/tree/master/cacti/CVE-2022-46169)

Cacti is a robust and extensible operational monitoring and fault management framework for users around the world. A command injection vulnerability allows an unauthenticated user to execute arbitrary code on a server running Cacti prior from version 1.2.17 to 1.2.22, if a specific data source was selected for any monitored device.

References:

- <https://github.com/Cacti/cacti/security/advisories/GHSA-6p93-p743-35gf>
- <https://mp.weixin.qq.com/s/6crwl8ggMkiHdeTtTApv3A>
- <https://nvd.nist.gov/vuln/detail/CVE-2022-46169>

## Vulnerability Environment

Execute following command to start a Cacti server 1.2.22:

```bash
# Compile environment
docker compose build

# Run environment
docker compose up -d
```

After the server is started, you will see the login page at `http://localhost:8080`.

Then login as admin/admin, follow the instructions to initialize the application. Actually, just click the "next button" again and again before you see the success page.

![](1.png)

Before you can exploit this vulnerability, you have to add a new "Graph" because the command injection is occurred not in the default graph type:

![](2.png)

Select the graph type "Device - Uptime", and click the "Create" button:

![](3.png)

## Exploit

After complete the above initialization, you will change your role to a attacker. Just send following request to Cacti server to trigger the command injection attack:

![](4.png)

Although no command result in the response, you can find the `/tmp/success` has been touched successfully.

![](5.png)

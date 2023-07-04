## Connecting to Remote Host from Local

### Via Command Line

1. Use `ssh` to connect to the remote host.

```bash
ssh aahmed@172.93.55.84
```

2. Type in your password when trying to connect.

- The password will not show up on the prompt so you have to remember the keys that you typed on the keyboard.

![](https://p131.p1.n0.cdn.getcloudapp.com/items/RBurrjyk/7a93f16f-f808-44bb-8b34-701bce4170a3.gif?v=b0313fc4432a3eae1f81501e50160dcc)

### Via Visual Studio Code

1. Open `Visual Studio Code`.

2. Install an extension called [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

![](https://p131.p1.n0.cdn.getcloudapp.com/items/WnummvDb/de13710a-9c80-472e-9594-d6a4f6a45a3e.jpg?v=999ce8171ccda50af163de55f2875bd3)

3. Open the Command Palette (Ctrl + Shift + P).

4. Select the option `Remote - SSH : Connect to Host`

5. Choose Add New Host

6. Pass in your ssh connection.

```bash
ssh aahmed@172.93.55.84
```

7. Select the first option for `sshconfig`.

8. Select `Connect` on bottom right notification.

![](https://p131.p1.n0.cdn.getcloudapp.com/items/eDurrOrQ/883a6648-2d3b-4428-bdb0-c8bab7beef5d.gif?v=18c4eb82eca22518c76fdf9f4be696cc)

9. Connect to the host. Type in password.

10. Open the new Visual Studio Code window.

- Follow this [video](https://share.getcloudapp.com/llu77LXv) for instructions.

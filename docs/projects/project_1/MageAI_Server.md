## Project 1: MageAI Server

### Details

- Host: `104.225.217.176`
- Port: `8371`
- Email: `admin@admin.com`
- Password: `admin`

### Docker Command

```bash
docker run --name ali_project_1_mageai \
           -e REQUIRE_USER_AUTHENTICATION=1 \
           -v $(pwd):/home/src \
           -p 8371:6789 \
           -itd mageai/mageai:latest
```

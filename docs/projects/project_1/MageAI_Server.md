## Project 1: MageAI Server

### Details

- Host: `104.225.217.176`
- Port: `8371`
- Email: `admin@admin.com`
- Password: `admin`
- [Link](http://104.225.217.176:8371)

### Docker Command

```bash
docker run --name ali_project_1_mageai \
           -e REQUIRE_USER_AUTHENTICATION=1 \
           -v $(pwd):/home/src \
           -p 8371:6789 \
           -itd mageai/mageai:latest \
           mage start aliexpress_sku_analysis
```

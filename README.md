# WEBSYS2020 サーバ・ネットワーク構築・運用 サンプルアプリ

# Install

Production Install

```sh
pip install -e "git+https://github.com/netmarkjp/websys2020-srvnet-example-app.git#egg=websys2020_srvnet_example_app[prod]"

cd /opt/websys2020-srvnet-example-app/app
export DJANGO_SETTINGS_MODULE=mysite.settings
export MYSITE_MY_CNF=/opt/websys2020-srvnet-example-app/venv/src/websys2020-srvnet-example-app/conf/my.cnf
export MYSITE_STATIC_ROOT=/opt/websys2020-srvnet-example-app/static
python3 manage.py migrate
python3 manage.py collectstatic
```

Development Install

```sh
pip install -e "git+https://github.com/netmarkjp/websys2020-srvnet-example-app.git#egg=websys2020_srvnet_example_app[dev]"
```

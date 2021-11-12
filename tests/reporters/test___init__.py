from telescope.reporters import AirflowReport, DAGReport, InfrastructureReport


def test_infrastructure_report_from_input_report_row(sample_report):
    actual = InfrastructureReport.from_input_report_row(sample_report["cluster_info"])
    expected = InfrastructureReport(
        type="k8s",
        provider="eks",
        version="v1.19.13-eks-8df270",
        num_nodes=6,
        allocatable_cpu=47.459999999999994,
        allocatable_gb=178,
        capacity_gb=184,
        capacity_cpu=48,
    )
    assert actual == expected


def test_airflow_report_from_input_report_row(sample_report):
    # AirflowReport.from_input_report_row(name=key, input_row=airflow_dict["airflow_report"])
    # "astronomer-amateur-cosmos-2865|amateur-cosmos-2865-scheduler-f55678947-fbn97": {
    name = "astronomer-amateur-cosmos-2865|amateur-cosmos-2865-scheduler-f55678947-dvj8v"
    actual = AirflowReport.from_input_report_row(
        name, sample_report["kubernetes"][name]["airflow_report"], sample_report["verify"]["helm"]
    )
    expected = AirflowReport(
        name=name,
        version="2.1.3+astro.1",
        executor="CeleryExecutor",
        num_schedulers=1,
        scheduler_resources="",
        num_webservers=1,
        num_workers=1,
        providers={
            "apache-airflow-providers-amazon": "1!2.1.0",
            "apache-airflow-providers-celery": "1!2.0.0",
            "apache-airflow-providers-cncf-kubernetes": "1!2.0.2",
            "apache-airflow-providers-elasticsearch": "1!2.0.2",
            "apache-airflow-providers-ftp": "1!2.0.0",
            "apache-airflow-providers-google": "1!5.0.0",
            "apache-airflow-providers-http": "1!2.0.0",
            "apache-airflow-providers-imap": "1!2.0.0",
            "apache-airflow-providers-microsoft-azure": "1!3.1.0",
            "apache-airflow-providers-mysql": "1!2.1.0",
            "apache-airflow-providers-postgres": "1!2.0.0",
            "apache-airflow-providers-redis": "1!2.0.0",
            "apache-airflow-providers-slack": "1!4.0.0",
            "apache-airflow-providers-sqlite": "1!2.0.0",
            "apache-airflow-providers-ssh": "1!2.1.0",
        },
        packages={
            "zope.interface": "5.4.0",
            "zope.event": "4.5.0",
            "zipp": "3.5.0",
            "wtforms": "2.3.3",
            "wheel": "0.37.0",
            "werkzeug": "1.0.1",
            "websocket-client": "1.2.1",
            "watchtower": "1.0.6",
            "virtualenv": "20.7.2",
            "vine": "1.3.0",
            "urllib3": "1.26.6",
            "uritemplate": "3.0.1",
            "unicodecsv": "0.14.1",
            "typing-inspect": "0.7.1",
            "typing-extensions": "3.7.4.3",
            "tornado": "6.1",
            "text-unidecode": "1.3",
            "termcolor": "1.1.0",
            "tenacity": "6.2.0",
            "tabulate": "0.8.9",
            "swagger-ui-bundle": "0.0.8",
            "statsd": "3.3.0",
            "sshtunnel": "0.1.5",
            "sqlalchemy": "1.3.24",
            "sqlalchemy-utils": "0.37.8",
            "sqlalchemy-jsonfield": "1.0.0",
            "sniffio": "1.2.0",
            "slack-sdk": "3.9.1",
            "six": "1.16.0",
            "setuptools": "57.4.0",
            "setproctitle": "1.2.2",
            "s3transfer": "0.4.2",
            "rsa": "4.7.2",
            "rich": "10.7.0",
            "rfc3986": "1.5.0",
            "requests": "2.26.0",
            "requests-oauthlib": "1.3.0",
            "redis": "3.5.3",
            "pyyaml": "5.4.1",
            "pytzdata": "2020.1",
            "pytz": "2021.1",
            "python3-openid": "3.2.0",
            "python-slugify": "4.0.1",
            "python-nvd3": "0.15.0",
            "python-editor": "1.0.4",
            "python-dateutil": "2.8.2",
            "python-daemon": "2.3.0",
            "pysftp": "0.2.9",
            "pyrsistent": "0.18.0",
            "pyparsing": "2.4.7",
            "pyopenssl": "20.0.1",
            "pynacl": "1.4.0",
            "pyjwt": "1.7.1",
            "pygments": "2.10.0",
            "pydata-google-auth": "1.2.0",
            "pycparser": "2.20",
            "pyasn1": "0.4.8",
            "pyasn1-modules": "0.2.8",
            "pyarrow": "4.0.1",
            "py": "1.10.0",
            "psycopg2-binary": "2.9.1",
            "psutil": "5.8.0",
            "protobuf": "3.17.3",
            "proto-plus": "1.19.0",
            "prometheus-client": "0.8.0",
            "prison": "0.1.3",
            "portalocker": "1.7.1",
            "platformdirs": "2.2.0",
            "pip": "21.2.4",
            "pendulum": "2.1.2",
            "paramiko": "2.7.2",
            "pandas": "1.3.2",
            "pandas-gbq": "0.14.1",
            "packaging": "20.9",
            "openapi-spec-validator": "0.3.1",
            "openapi-schema-validator": "0.1.5",
            "oauthlib": "3.1.1",
            "numpy": "1.20.3",
            "nox": "2020.12.31",
            "mysqlclient": "2.0.3",
            "mysql-connector-python": "8.0.22",
            "mypy-extensions": "0.4.3",
            "msrestazure": "0.6.4",
            "msrest": "0.6.21",
            "msal": "1.13.0",
            "msal-extensions": "0.3.0",
            "marshmallow": "3.13.0",
            "marshmallow-sqlalchemy": "0.23.1",
            "marshmallow-oneofschema": "3.0.1",
            "marshmallow-enum": "1.5.1",
            "markupsafe": "1.1.1",
            "markdown": "3.3.4",
            "mako": "1.1.4",
            "lockfile": "0.12.2",
            "libcst": "0.3.20",
            "lazy-object-proxy": "1.4.3",
            "kubernetes": "11.0.0",
            "kombu": "4.6.11",
            "jwcrypto": "0.6.0",
            "jsonschema": "3.2.0",
            "json-merge-patch": "0.2",
            "jmespath": "0.10.0",
            "jinja2": "2.11.3",
            "itsdangerous": "1.1.0",
            "isodate": "0.6.0",
            "iso8601": "0.1.16",
            "inflection": "0.5.1",
            "importlib-resources": "1.5.0",
            "importlib-metadata": "4.6.4",
            "idna": "3.2",
            "humanize": "3.11.0",
            "httpx": "0.18.2",
            "httplib2": "0.19.1",
            "httpcore": "0.13.6",
            "h11": "0.12.0",
            "gunicorn": "20.1.0",
            "grpcio": "1.39.0",
            "grpcio-gcp": "0.2.2",
            "grpc-google-iam-v1": "0.12.3",
            "greenlet": "1.1.1",
            "graphviz": "0.17",
            "googleapis-common-protos": "1.53.0",
            "google-resumable-media": "1.3.3",
            "google-crc32c": "1.1.2",
            "google-cloud-workflows": "1.2.1",
            "google-cloud-vision": "1.0.0",
            "google-cloud-videointelligence": "1.16.1",
            "google-cloud-translate": "1.7.0",
            "google-cloud-texttospeech": "1.0.1",
            "google-cloud-tasks": "2.5.1",
            "google-cloud-storage": "1.42.0",
            "google-cloud-speech": "1.3.2",
            "google-cloud-spanner": "1.19.1",
            "google-cloud-secret-manager": "1.0.0",
            "google-cloud-redis": "2.2.2",
            "google-cloud-pubsub": "2.7.0",
            "google-cloud-os-login": "2.3.1",
            "google-cloud-monitoring": "2.4.2",
            "google-cloud-memcache": "1.0.0",
            "google-cloud-logging": "2.6.0",
            "google-cloud-language": "1.3.0",
            "google-cloud-kms": "2.5.0",
            "google-cloud-dlp": "1.0.0",
            "google-cloud-dataproc": "2.5.0",
            "google-cloud-datacatalog": "3.4.0",
            "google-cloud-core": "1.7.2",
            "google-cloud-container": "1.0.1",
            "google-cloud-bigtable": "1.7.0",
            "google-cloud-bigquery": "2.24.0",
            "google-cloud-bigquery-storage": "2.6.3",
            "google-cloud-bigquery-datatransfer": "3.3.1",
            "google-cloud-automl": "2.4.2",
            "google-cloud-audit-log": "0.1.0",
            "google-cloud-appengine-logging": "0.1.4",
            "google-auth": "1.35.0",
            "google-auth-oauthlib": "0.4.5",
            "google-auth-httplib2": "0.1.0",
            "google-api-python-client": "1.12.8",
            "google-api-core": "1.31.2",
            "google-ads": "13.0.0",
            "gevent": "21.8.0",
            "flower": "0.9.7",
            "flask": "1.1.4",
            "flask-wtf": "0.14.3",
            "flask-sqlalchemy": "2.5.1",
            "flask-openid": "1.2.5",
            "flask-login": "0.4.1",
            "flask-jwt-extended": "3.25.1",
            "flask-caching": "1.10.1",
            "flask-bcrypt": "0.7.1",
            "flask-babel": "1.0.0",
            "flask-appbuilder": "3.3.2",
            "filelock": "3.0.12",
            "eventlet": "0.31.1",
            "email-validator": "1.1.3",
            "elasticsearch": "7.13.4",
            "elasticsearch-dsl": "7.4.0",
            "elasticsearch-dbapi": "0.2.4",
            "docutils": "0.16",
            "dnspython": "1.16.0",
            "distro": "1.6.0",
            "distlib": "0.3.2",
            "dill": "0.3.1.1",
            "defusedxml": "0.7.1",
            "cryptography": "3.4.7",
            "croniter": "1.0.15",
            "commonmark": "0.9.1",
            "colorlog": "4.8.0",
            "colorama": "0.4.4",
            "clickclick": "20.10.2",
            "click": "7.1.2",
            "charset-normalizer": "2.0.4",
            "cffi": "1.14.6",
            "certifi": "2020.12.5",
            "celery": "4.4.7",
            "cattrs": "1.5.0",
            "cachetools": "4.2.2",
            "cached-property": "1.5.2",
            "botocore": "1.20.112",
            "boto3": "1.17.112",
            "blinker": "1.4",
            "billiard": "3.6.4.0",
            "bcrypt": "3.2.0",
            "backports.entry-points-selectable": "1.1.0",
            "babel": "2.9.1",
            "azure-storage-file": "2.1.0",
            "azure-storage-common": "2.1.0",
            "azure-storage-blob": "12.8.1",
            "azure-nspkg": "3.0.2",
            "azure-mgmt-resource": "19.0.0",
            "azure-mgmt-nspkg": "3.0.2",
            "azure-mgmt-datalake-store": "0.5.0",
            "azure-mgmt-datalake-nspkg": "3.0.1",
            "azure-mgmt-datafactory": "1.1.0",
            "azure-mgmt-core": "1.3.0",
            "azure-mgmt-containerinstance": "1.5.0",
            "azure-kusto-data": "0.0.45",
            "azure-keyvault": "4.1.0",
            "azure-keyvault-secrets": "4.3.0",
            "azure-keyvault-keys": "4.4.0",
            "azure-keyvault-certificates": "4.3.0",
            "azure-identity": "1.6.0",
            "azure-datalake-store": "0.0.52",
            "azure-cosmos": "3.2.0",
            "azure-core": "1.17.0",
            "azure-common": "1.1.27",
            "azure-batch": "11.0.0",
            "attrs": "20.3.0",
            "astronomer-fab-security-manager": "1.6.0",
            "astronomer-certified": "2.1.3.post1",
            "astronomer-airflow-version-check": "1.0.7",
            "astronomer-airflow-scripts": "0.0.5",
            "argcomplete": "1.12.3",
            "apispec": "3.3.2",
            "apache-airflow": "1!2.1.3+astro.1",
            "apache-airflow-providers-ssh": "1!2.1.0",
            "apache-airflow-providers-sqlite": "1!2.0.0",
            "apache-airflow-providers-slack": "1!4.0.0",
            "apache-airflow-providers-redis": "1!2.0.0",
            "apache-airflow-providers-postgres": "1!2.0.0",
            "apache-airflow-providers-mysql": "1!2.1.0",
            "apache-airflow-providers-microsoft-azure": "1!3.1.0",
            "apache-airflow-providers-imap": "1!2.0.0",
            "apache-airflow-providers-http": "1!2.0.0",
            "apache-airflow-providers-google": "1!5.0.0",
            "apache-airflow-providers-ftp": "1!2.0.0",
            "apache-airflow-providers-elasticsearch": "1!2.0.2",
            "apache-airflow-providers-cncf-kubernetes": "1!2.0.2",
            "apache-airflow-providers-celery": "1!2.0.0",
            "apache-airflow-providers-amazon": "1!2.1.0",
            "anyio": "3.3.0",
            "amqp": "2.6.1",
            "alembic": "1.6.5",
            "adal": "1.2.7",
        },
        non_default_configurations={
            "core.executor": ["CeleryExecutor", "airflow.cfg"],
            "core.sql_alchemy_conn": ["***", "env var"],
            "core.load_examples": ["False", "airflow.cfg"],
            "core.fernet_key": ["aHpHYXpCVmdDcjVWdHZ2ckNzc2JsZDVHeWZhNDRnNFA=", "env var"],
            "core.colored_console_log": ["False", "airflow.cfg"],
            "core.remote_logging": ["True", "airflow.cfg"],
            "logging.remote_logging": ["True", "airflow.cfg"],
            "logging.colored_console_log": ["False", "airflow.cfg"],
            "metrics.statsd_on": ["True", "airflow.cfg"],
            "metrics.statsd_host": ["amateur-cosmos-2865-statsd", "airflow.cfg"],
            "metrics.statsd_port": ["9125", "airflow.cfg"],
            "metrics.statsd_prefix": ["airflow", "airflow.cfg"],
            "webserver.base_url": [
                "https://deployments.aws.solutions.astronomer-sandbox.io/amateur-cosmos-2865/airflow",
                "airflow.cfg",
            ],
            "webserver.expose_config": ["True", "env var"],
            "webserver.enable_proxy_fix": ["True", "airflow.cfg"],
            "webserver.rbac": ["True", "airflow.cfg"],
            "celery.broker_url": ["***", "env var"],
            "celery.result_backend": ["***", "env var"],
            "celery.default_queue": ["celery", "airflow.cfg"],
            "celery.celery_result_backend": [
                "db+postgresql://amateur_cosmos_2865_celery:Hy0oDcnGQ5vVRHxLiFfRPZzCCrRgqTuY@amateur-cosmos-2865-pgbouncer:6543/amateur-cosmos-2865-result-backend?sslmode=disable",
                "env var",
            ],
            "scheduler.scheduler_heartbeat_sec": ["5", "airflow.cfg"],
            "scheduler.statsd_on": ["True", "airflow.cfg"],
            "scheduler.statsd_port": ["9125", "airflow.cfg"],
            "scheduler.statsd_prefix": ["airflow", "airflow.cfg"],
            "scheduler.statsd_host": ["amateur-cosmos-2865-statsd", "airflow.cfg"],
            "scheduler.run_duration": ["41460", "airflow.cfg"],
            "elasticsearch.host": [
                "http://amateur-cosmos-2865:gHm4ALq3hDTyK2GrzDfZDHMgPUCKOwzG@astronomer-elasticsearch-nginx.astronomer:9200",
                "env var",
            ],
            "elasticsearch.log_id_template": ["{dag_id}_{task_id}_{execution_date}_{try_number}", "airflow.cfg"],
            "elasticsearch.write_stdout": ["True", "airflow.cfg"],
            "elasticsearch.json_format": ["True", "airflow.cfg"],
            "elasticsearch.elasticsearch_write_stdout": ["True", "airflow.cfg"],
            "elasticsearch.elasticsearch_json_format": ["True", "airflow.cfg"],
            "elasticsearch.elasticsearch_log_id_template": [
                "{dag_id}_{task_id}_{execution_date}_{try_number}",
                "airflow.cfg",
            ],
            "elasticsearch.elasticsearch_host": [
                "http://amateur-cosmos-2865:gHm4ALq3hDTyK2GrzDfZDHMgPUCKOwzG@astronomer-elasticsearch-nginx.astronomer:9200",
                "env var",
            ],
            "elasticsearch_configs.max_retries": ["3", "airflow.cfg"],
            "elasticsearch_configs.timeout": ["30", "airflow.cfg"],
            "elasticsearch_configs.retry_timeout": ["True", "airflow.cfg"],
            "kubernetes.pod_template_file": ["/usr/local/airflow/pod_templates/pod_template_file.yaml", "airflow.cfg"],
            "kubernetes.worker_container_repository": [
                "registry.aws.solutions.astronomer-sandbox.io/amateur-cosmos-2865/airflow",
                "airflow.cfg",
            ],
            "kubernetes.worker_container_tag": ["deploy-3", "airflow.cfg"],
            "kubernetes.namespace": ["astronomer-amateur-cosmos-2865", "airflow.cfg"],
            "kubernetes.delete_worker_pods": ["True", "airflow.cfg"],
            "kubernetes.airflow_configmap": ["amateur-cosmos-2865-airflow-config", "airflow.cfg"],
            "kubernetes.airflow_local_settings_configmap": ["amateur-cosmos-2865-airflow-config", "airflow.cfg"],
            "kubernetes.worker_container_image_pull_policy": ["IfNotPresent", "airflow.cfg"],
            "kubernetes.dags_in_image": ["True", "airflow.cfg"],
            "astronomer.jwt_signing_cert": ["/etc/airflow/tls/tls.crt", "airflow.cfg"],
            "astronomer.jwt_audience": [
                "deployments.aws.solutions.astronomer-sandbox.io/amateur-cosmos-2865",
                "airflow.cfg",
            ],
            "kubernetes_secrets.airflow__webserver__expose_config": ["***", "env var"],
        },
        pools={"default_pool": {"total": 128, "running": 0, "queued": 0, "open": 128}},
        env={
            "config_options": [
                "AIRFLOW__WEBSERVER__EXPOSE_CONFIG",
                "AIRFLOW__KUBERNETES_SECRETS__AIRFLOW__WEBSERVER__EXPOSE_CONFIG",
                "AIRFLOW__ELASTICSEARCH__ELASTICSEARCH_HOST",
                "AIRFLOW__CORE__SQL_ALCHEMY_CONN",
                "AIRFLOW__CORE__FERNET_KEY",
                "AIRFLOW__ELASTICSEARCH__HOST",
                "AIRFLOW__CELERY__RESULT_BACKEND",
                "AIRFLOW__CELERY__CELERY_RESULT_BACKEND",
                "AIRFLOW__CELERY__BROKER_URL",
            ],
            "connections": ["AIRFLOW_CONN_AIRFLOW_DB"],
            "variables": [],
        },
        connections=["AIRFLOW_CONN_AIRFLOW_DB", "my-test-connection", "my-other-test-connection"],
        task_run_info={"total": 72, "1_day": 0, "7_days": 0, "30_days": 0, "365_days": 72},
    )
    assert actual == expected


def test_dag_report_from_input_report_row(sample_report):
    name = "astronomer-amateur-cosmos-2865|amateur-cosmos-2865-scheduler-f55678947-dvj8v"
    actual = DAGReport(airflow_name=name, **sample_report["kubernetes"][name]["airflow_report"]["dags_report"][0])
    expected = DAGReport(
        airflow_name=name,
        dag_id="triggered_by_api",
        root_dag_id=None,
        is_active=True,
        is_paused=False,
        is_subdag=False,
        schedule_interval=None,
        fileloc="/usr/local/airflow/dags/cross-deployment-downstream-dag/cross-deployment-downstream-dag.py",
        owners="airflow",
        operators="DummyOperator,PythonOperator",
        num_tasks=3,
        connections="",
        variables="",
    )

    print(actual)
    assert actual == expected

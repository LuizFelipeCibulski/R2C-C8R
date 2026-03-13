from kubernetes import client, config

custom_config_path=("/app/config")

config.load_kube_config(config_file=custom_config_path)

v1 = client.CoreV1Api()

def create_user(username, namespace):

    sa = client.V1ServiceAccount(
        metadata=client.V1ObjectMeta(
            name=username
        )
    )

    v1.create_namespaced_service_account(
        namespace=namespace,
        body=sa
    )
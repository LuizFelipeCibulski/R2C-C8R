from kubernetes import client

rbac = client.RbacAuthorizationV1Api()

def bind_sa_to_role(sa, namespace, role):

    rb = client.V1RoleBinding(
        metadata=client.V1ObjectMeta(
            name=f"{sa}-binding"
        ),
        subjects=[
            client.V1Subject(
                kind="ServiceAccount",
                name=sa,
                namespace=namespace
            )
        ],
        role_ref=client.V1RoleRef(
            kind="Role",
            name=role,
            api_group="rbac.authorization.k8s.io"
        )
    )

    rbac.create_namespaced_role_binding(namespace, rb)
from telescope.getters.kubernetes import KubernetesGetter


def cluster_info(getter: KubernetesGetter):
    def cloud_provider(o):
        if "gke" in o:
            return "gke"
        elif "eks" in o:
            return "eks"
        elif "az" in o:
            return "aks"
        else:
            return None

    def parse_cpu(cpu):
        if "m" in cpu:
            return int(cpu[:-1]) / 1000
        else:
            return int(cpu)

    def parse_mem(mem):
        # if 'Ki' in mem:
        return int(mem[:-2])

    res = getter.api_client.get_code()
    nodes_res = getter.kube_client.list_node()
    return {
        "type": "k8s",
        "version": res.git_version,
        "provider": cloud_provider(res.git_version),
        "allocatable_cpu": sum(parse_cpu(r.status.allocatable["cpu"]) for r in nodes_res.items),
        "allocatable_gb": int(sum(parse_mem(r.status.allocatable["memory"]) for r in nodes_res.items) / 1024 ** 2),
        "capacity_cpu": sum(parse_cpu(r.status.capacity["cpu"]) for r in nodes_res.items),
        "capacity_gb": int(sum(parse_mem(r.status.capacity["memory"]) for r in nodes_res.items) / 1024 ** 2),
    }

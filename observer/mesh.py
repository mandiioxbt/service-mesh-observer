class ServiceMeshObserver:
    def __init__(self, mesh="istio"): self.mesh, self.services = mesh, {}
    def discover(self): return []
    def traffic_flow(self, src, dst): return {"source": src, "dest": dst, "rps": 0, "errors": 0}
    def health(self, svc): return {"service": svc, "status": "healthy", "pods": 3}

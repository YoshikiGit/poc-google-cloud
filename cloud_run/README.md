## ソースから Cloud Run にデプロイ

```console
gcloud run deploy --source .
```

## Dockerfileを用意して、Cloud Buildでbuildしてpush

```console
gcloud builds submit --tag asia-northeast1-docker.pkg.dev/project-id/cloud-run-source-deploy/poc-google-cloud/cr-hello-world:latest
```

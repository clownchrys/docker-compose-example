# Stage 1. App 컴파일을 위한 스테이지
FROM golang:1.14.1-alpine3.11 as builder

COPY ./main.go ./
RUN go build -o /go-app ./main.go





# Stage 2. 컴파일한 바이너리를 포함하는 실행용 스테이지
FROM alpine:3.11

# Stage 1에서 컴파일한 결과(/go-app)를 실행용 컨테이너에 복사
COPY --from=builder /go-app .
ENTRYPOINT ["./go-app"]
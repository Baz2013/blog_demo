FROM xiabingxiejiang/redis_base:latest
MAINTAINER xiabingxiejiang <chuan.gu6@gamil.com>
ENV REFRESHED_AT 2016-07-04

ENTRYPOINT [ "redis-server", "--logfile /var/log/redis/redis-replica.log", "--slaveof redis_primary 6379" ]

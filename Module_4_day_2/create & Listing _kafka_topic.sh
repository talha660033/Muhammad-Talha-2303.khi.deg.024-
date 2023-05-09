#!/bin/bash

docker compose exec broker kafka-topics --create --topic events -partitions 3 --bootstrap-server broker:9092

docker compose exec broker kafka-topics --create --topic newkafka --partitions 3 --bootstrap-server broker:9092

docker compose exec broker kafka-topics --list --bootstrap-server broker:9092






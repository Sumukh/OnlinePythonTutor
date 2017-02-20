all: copy build clean

copy:
	cp ../../../v5-unity/pg_logger.py . && cp ../../../v5-unity/pg_encoder.py .

build:
	docker build -t="pgbovine/cokapi-py3:v1" .

clean:
	rm pg_logger.py && rm pg_encoder.py

test:
	docker run -t -i --rm --user=netuser --net=none --cap-drop all pgbovine/cokapi-py3:v1 sh run_tests.sh

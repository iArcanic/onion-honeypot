# Use base Logstash image
FROM docker.elastic.co/logstash/logstash:8.13.1

# Copy custom Logstash configuration file
COPY config/logstash.yml /usr/share/logstash/config/logstash.yml

# Copy Logstash pipeline file
COPY pipeline/logstash.conf /usr/share/logstash/pipeline/logstash.conf

# Expose Logstash ports
EXPOSE 5044
EXPOSE 5514
EXPOSE 9600

# Start Logstash
CMD ["logstash"]
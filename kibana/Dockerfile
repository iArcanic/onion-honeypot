# Use base Kibana image
FROM docker.elastic.co/kibana/kibana:8.13.1

# Copy custom Kibana configuration file
COPY config/kibana.yml /usr/share/kibana/config/kibana.yml

# Expose Kibana port
EXPOSE 5601

# Start Kibana
CMD ["kibana"]
# Use base Elasticsearch image
FROM docker.elastic.co/elasticsearch/elasticsearch:8.13.1

# Copy custom Elasticsearch configuration file
COPY config/elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

# Expose Elasticsearch ports
EXPOSE 9200
EXPOSE 9300

# Start Elasticsearch
CMD ["elasticsearch"]
# Use the official Cassandra image from Docker Hub
FROM cassandra:latest

# Expose the necessary ports
EXPOSE 7000 7001 7199 9042 9160

# Set the working directory (optional, can be skipped)
WORKDIR /usr/local/cassandra

# Run Cassandra (this will be the default command)
CMD ["cassandra", "-f"]

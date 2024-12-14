#!/usr/bin/env bash
set -e

# Update package index and install Java 17
sudo apt-get update
sudo apt-get install -y openjdk-17-jdk

# Verify Java installation and set JAVA_HOME
JAVA_BIN=$(which java)
JAVA_HOME=$(dirname $(dirname $(readlink -f $JAVA_BIN)))
export JAVA_HOME=$JAVA_HOME

# Initialize conda. Adjust the path to conda if necessary.
source "$(conda info --base)/etc/profile.d/conda.sh"

# Create a new conda environment with Python 3.10
conda create --name spark_env python=3.10 -y

# Activate the new environment
conda activate spark_env

# Install PySpark and optional packages
conda install -c conda-forge pyspark pandas numpy jupyter -y

echo "=== Installation Complete ==="
echo "JAVA_HOME is set to: $JAVA_HOME"
echo "Python version:"
python --version
echo "PySpark version:"
pyspark --version

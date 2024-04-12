terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.45.0"
    }
  }
}

provider "aws" {
  # Configuration options
  access_key = ""
  secret_key = ""
  region = "ap-south-1"
}

resource "aws_instance" "webserver1" {
  ami                    = "ami-007020fd9c84e18c7"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [sg-00e239015e45bcb80]
  subnet_id              = subnet-0713506a0f78c0d52
  key_name               = "test-st"           #var.key_name
  user_data              = base64encode(file("userdata.sh"))
  tags = {
    Name = "html-test"
  }

}
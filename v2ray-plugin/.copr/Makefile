.PHONY: srpm
.DEFAULT_GOAL := srpm

DOT_COPR := $(dir $(firstword $(MAKEFILE_LIST)))
TOP_DIR := $(realpath $(DOT_COPR)/../)

RPM_DIR := $(TOP_DIR)/
outdir ?= $(RPM_DIR)/SRPMS


srpm:
	$(TOP_DIR)/generate_source.bash

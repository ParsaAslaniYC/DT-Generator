#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from aospdtgen.proprietary_files.section import Section, register_section

class SoterSection(Section):
	name = "Soter"
	interfaces = [
		"vendor.qti.hardware.soter",
	]
	apps = [
		"SoterService",
	]

register_section(SoterSection)

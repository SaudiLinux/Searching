#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Infected Links Report - Israeli Website URLs Report
"""

class InfectedLinksReport:
    def __init__(self):
        pass

    def generate(self):
        print("Generating infected links report...")
        
        # Basic infected sites data
        infected_sites = [
            {
                "domain": "gov.il",
                "url": "https://www.gov.il",
                "type": "Government",
                "severity": "HIGH",
                "description": "Israeli Government Portal"
            },
            {
                "domain": "ynet.co.il", 
                "url": "https://www.ynet.co.il",
                "type": "News",
                "severity": "HIGH", 
                "description": "Ynet - Israeli News Portal"
            },
            {
                "domain": "haaretz.co.il",
                "url": "https://www.haaretz.co.il", 
                "type": "Newspaper",
                "severity": "HIGH",
                "description": "Haaretz Israeli Newspaper"
            },
            {
                "domain": "jpost.com",
                "url": "https://www.jpost.com",
                "type": "News",
                "severity": "HIGH",
                "description": "Jerusalem Post - Israeli News"
            },
            {
                "domain": "timesofisrael.com",
                "url": "https://www.timesofisrael.com",
                "type": "Online News",
                "severity": "MEDIUM",
                "description": "Times of Israel - Israeli News Site"
            }
        ]
        
        return infected_sites
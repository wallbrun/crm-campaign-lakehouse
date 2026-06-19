# CRM Campaign Lakehouse

## Overview

Projeto de Analytics Engineering inspirado em cenários corporativos de CRM e Customer Analytics.

O pipeline implementa arquitetura Medallion (Bronze, Silver e Gold) para ingestão, tratamento, enriquecimento e disponibilização de métricas de negócio para análise de campanhas e segmentação de clientes.

## Arquitetura

RAW → Bronze → Silver → Gold → Semantic Layer → DuckDB → Power BI

## Tecnologias

* Python
* Pandas
* Parquet
* DuckDB
* Power BI
* Git

## Métricas de Clientes

* Receita Total
* Ticket Médio
* Quantidade de Compras
* Última Compra
* Segmentação de Clientes

## Métricas de Campanha

* Clientes Impactados
* Taxa de Abertura
* CTR
* Taxa de Conversão

## Conceitos Aplicados

* Analytics Engineering
* Medallion Architecture
* Semantic Layer
* Customer Analytics
* Campaign Analytics
* Business Metrics
* Data Quality
* Data Modeling
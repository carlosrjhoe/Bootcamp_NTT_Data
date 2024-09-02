# Bootcamp_NTT_Data

# Desafio 01: Sistema Bancário em Python

Este é um simples sistema bancário desenvolvido em Python. O programa permite que o usuário realize as principais operações bancárias de forma interativa, como:

- Depositar dinheiro em sua conta.
- Sacar dinheiro, com limite diário de 3 saques e valor máximo de R$500 por saque.
- Visualizar o extrato das movimentações, incluindo depósitos e saques realizados.
- Sair do sistema quando desejar.

O sistema é fácil de usar e foi feito para ajudar a gerenciar uma conta bancária fictícia.

# Desafio 02: Implementação do sistema bancário
Na segunda fase do nosso sistema bancário, adicionamos funcionalidades para gerenciar clientes e contas bancárias. Agora, é possível cadastrar novos usuários e criar contas para eles.

Principais mudanças:

- Cadastro de Usuário: Adicionamos uma função para registrar novos clientes com nome e CPF.
- Cadastro de Conta Bancária: Implementamos uma função para criar contas bancárias associadas a um cliente existente.
- Operações Bancárias: As funções de depósito e saque foram ajustadas para operar com base no número da conta bancária. O saldo e o extrato agora são específicos para cada conta.
- Visualização de Extrato: Também incluímos a opção de visualizar o extrato de cada conta, mostrando todas as movimentações e o saldo atual.

Essas melhorias tornam o sistema mais completo e pronto para gerenciar diferentes contas e usuários.

# Desafio 03: Mudança de Paradigma Funcional para Programação Orientada a Objetos (POO) e modularização

Principais mudanças:

A decisão de adotar POO foi guiada pela necessidade de melhorar a organização e a manutenção do código, além de facilitar a reutilização de componentes e a expansão futura do sistema. Com POO, conseguimos encapsular responsabilidades em classes, promovendo um design modular que se alinha mais naturalmente ao modelo de um sistema bancário, onde conceitos como "Conta", "Transação" e "Histórico" são abstrações claras e independentes.

- Encapsulamento: Ao encapsular atributos e comportamentos dentro de classes, reduzimos a complexidade do código e facilitamos o rastreamento de estados e a depuração.
- Reutilização de Código: A introdução de classes base, como Transacao, permite que diferentes tipos de transações (como Deposito e Saque) compartilhem código comum, reduzindo redundâncias.
- Extensibilidade: Com POO, ficou mais fácil adicionar novos tipos de transações ou funcionalidades ao sistema, simplesmente estendendo as classes existentes.
- Histórico de Transações: Agora, cada transação registra automaticamente a data e hora em que foi realizada, armazenando esses dados no histórico da conta de forma organizada.

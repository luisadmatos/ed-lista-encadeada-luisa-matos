### Atividade 1 — Reconhecimento das operações
'''
Considere o deque representado a seguir:

**start** → [8, 4, 7, 2, 5] ← **end**

Com base nessa representação, responda:

1. Qual elemento está na extremidade inicial?
2. Qual elemento está na extremidade final?
3. Qual operação deve ser utilizada para inserir o valor `10` no início?
4. Qual operação deve ser utilizada para inserir o valor `10` no final?
5. Qual operação remove o elemento `8`?
6. Qual operação remove o elemento `5`?

Escreva suas respostas no bloco abaixo.
'''
respostas_atividade_1 = {
    "1. Qual elemento está na extremidade inicial?": "8",
    "2. Qual elemento está na extremidade final?": "5",
    "3. Qual operação para inserir 10 no início?": "add_front() ou add_start()",
    "4. Qual operação para inserir 10 no final?": "add_rear() ou add_end()",
    "5. Qual operação remove o elemento 8?": "remove_front() ou remove_start()",
    "6. Qual operação remove o elemento 5?": "remove_rear() ou remove_end()"
}

for pergunta, resposta in respostas_atividade_1.items():
    print(f"{pergunta}\nResposta: {resposta}\n")


### Atividade 2 — Teste de mesa da remoção no final
'''
Considere o trecho abaixo, usado para percorrer uma lista simplesmente encadeada:

```python
pointer = self.head
prev = None

while pointer:
    prev = pointer
    pointer = pointer.next
```

Suponha que o deque esteja no seguinte estado:

**start** → [8, 4, 7, 2, 5] ← **end**

Preencha a tabela a seguir, indicando os valores de `pointer` e `prev` ao longo da execução.

| Iteração | `pointer.data` | `prev.data` |
|---|---:|---:|
| Inicial |   |   |
| 1 |   |   |
| 2 |   |   |
| 3 |   |   |
| 4 |   |   |
| 5 |   |   |
| Final |   |   |

Ao final, responda: esse laço faz `prev` apontar para o último nó ou para o penúltimo?
'''

#RESPOSTA: Ao final, `prev` aponta para o ÚLTIMO NÓ (elemento 5).
#Isso ocorre porque quando pointer chega a None, prev ainda aponta para o último nó.

print("Teste de mesa da Atividade 2:")
print("=" * 60)
print("\nSimulação da traversal:")
print("Iteração | pointer.data | prev.data")
print("---------|---|---")
print("Inicial  | (None)       | (None)")
print("1        | 8            | (None)")
print("2        | 4            | 8")
print("3        | 7            | 4")
print("4        | 2            | 7")
print("5        | 5            | 2")
print("Final    | (None)       | 5")
print("\n✓ CONCLUSÃO: prev aponta para o ÚLTIMO NÓ (elemento 5)")


### Atividade 3 — Identificação do erro lógico
'''
Analise a implementação abaixo.

```python
def remove_end(self):
    if self._size == 0:
        raise IndexError("The queue is empty")    

    elem = self.tail.data
    pointer = self.head
    prev = None

    while pointer:
        prev = pointer
        pointer = pointer.next

    prev.next = None
    self.tail = prev
    self._size = self._size - 1

    return elem
```

Responda:

1. Qual é o erro lógico principal dessa implementação?
2. Após o laço, `prev` referencia qual nó?
3. Por que a instrução `prev.next = None` não remove corretamente o último elemento nesse caso?
4. O que deveria ser encontrado antes de atualizar `self.tail`?
'''

print("ANÁLISE DO CÓDIGO remove_end():\n")
analise = """
def remove_end(self):
    if self._size == 0:
        raise IndexError("The queue is empty")    
    elem = self.tail.data
    pointer = self.head
    prev = None
    
    while pointer:
        prev = pointer
        pointer = pointer.next
    
    prev.next = None
    self.tail = prev
    self._size = self._size - 1
    
    return elem
"""

print(analise)
print("\n" + "="*70)
print("RESPOSTAS:\n")

print("1. Qual é o erro lógico principal dessa implementação?")
print("   ✗ ERRO: O laço percorre ATÉ O FINAL, fazendo `prev` apontar para")
print("     o ÚLTIMO nó (aquele a ser removido).")
print("   ✓ CORRETO: Deveria parar no PENÚLTIMO nó para poder remover o último.\n")

print("2. Após o laço, `prev` referencia qual nó?")
print("   → O ÚLTIMO nó (elemento 5)\n")

print("3. Por que `prev.next = None` não remove corretamente?")
print("   → Porque `prev` aponta para o nó a ser removido (tail).")
print("   → Removendo o próprio tail deixaria referências inválidas.\n")

print("4. O que deveria ser encontrado antes de atualizar `self.tail`?")
print("   → O PENÚLTIMO nó (o nó anterior ao tail).")
print("   → Assim podemos fazer: penultimo.next = None e tail = penultimo\n")

print("="*70)
print("\n✓ SOLUÇÃO CORRETA:")
print("""
def remove_end(self):
    if self._size == 0:
        raise IndexError("The queue is empty")    
    
    if self._size == 1:  # Caso especial: apenas um elemento
        elem = self.head.data
        self.head = None
        self.tail = None
        self._size = 0
        return elem
    
    elem = self.tail.data
    pointer = self.head
    prev = None
    
    # Parar ANTES do último nó
    while pointer.next:  # ← NOTE: pointer.next, não apenas pointer
        prev = pointer
        pointer = pointer.next
    
    pointer.next = None
    self.tail = pointer
    self._size -= 1
    
    return elem
""")



### Atividade 4 — Casos de borda
'''
Explique o que deveria acontecer em cada uma das situações abaixo ao executar `remove_end()`:

1. O deque está vazio.
2. O deque possui apenas um elemento.
3. O deque possui dois elementos.
4. O deque possui vários elementos.

Para cada caso, descreva:
- o valor retornado;
- o novo valor de `head`;
- o novo valor de `tail`;
- o novo valor de `_size`.


print("ANÁLISE: remove_end() em diferentes casos\n")
print("="*80)

casos = {
    "1. Deque vazio": {
        "Retorno": "Levanta IndexError('The queue is empty')",
        "head": "N/A (exceção)",
        "tail": "N/A (exceção)",
        "_size": "0 (não muda)"
    },
    "2. Um elemento": {
        "Retorno": "Retorna o valor do elemento",
        "head": "None",
        "tail": "None",
        "_size": "0"
    },
    "3. Dois elementos": {
        "Retorno": "Retorna o segundo elemento",
        "head": "Aponta para o primeiro elemento",
        "tail": "Aponta para o primeiro elemento (agora é o último)",
        "_size": "1"
    },
    "4. Vários elementos": {
        "Retorno": "Retorna o último elemento",
        "head": "Sem mudança",
        "tail": "Aponta para o penúltimo elemento",
        "_size": "Decrementado de 1"
    }
}

for caso, detalhes in casos.items():
    print(f"\n{caso}:")
    print("-" * 80)
    for chave, valor in detalhes.items():
        print(f"  • {chave:15} → {valor}")
'''

### Atividade 5 — Análise de complexidade
'''
Responda às perguntas abaixo.

1. Qual é a complexidade da operação `add_start()`?
2. Qual é a complexidade da operação `add_end()`?
3. Qual é a complexidade da operação `remove_start()`?
4. Qual é a complexidade da operação `remove_end()` nessa implementação?
5. Por que `remove_end()` não é `O(1)` em uma lista simplesmente encadeada?
'''

print("ANÁLISE DE COMPLEXIDADE DAS OPERAÇÕES DO DEQUE\n")
print("="*80)

operacoes = {
    "1. add_start()": {
        "Complexidade": "O(1)",
        "Motivo": "Insere direto no head, sem percurso",
        "Operações": "Criar nó + atualizar 2 ponteiros"
    },
    "2. add_end()": {
        "Complexidade": "O(1)",
        "Motivo": "Insere direto no tail, sem percurso",
        "Operações": "Criar nó + atualizar 2 ponteiros"
    },
    "3. remove_start()": {
        "Complexidade": "O(1)",
        "Motivo": "Remove direto do head, sem percurso",
        "Operações": "Atualizar head + desalocar nó"
    },
    "4. remove_end() [lista simples]": {
        "Complexidade": "O(n)",
        "Motivo": "Precisa percorrer TODA a lista até encontrar o penúltimo",
        "Operações": "Percorrer n-1 nós + atualizar tail"
    }
}

for operacao, info in operacoes.items():
    print(f"\n{operacao}")
    print("-" * 80)
    for chave, valor in info.items():
        print(f"  • {chave:20} → {valor}")

print("\n" + "="*80)
print("\n5. Por que remove_end() NÃO é O(1) em lista simplesmente encadeada?\n")

explicacao = """
Em uma lista SIMPLESMENTE encadeada:
  • Cada nó tem APENAS um ponteiro (para o próximo)
  • Não há ponteiro para trás (para o anterior)
  • O tail aponta para o ÚLTIMO nó

Para remover o último elemento:
  • Precisamos atualizar o tail para o PENÚLTIMO nó
  • Mas como encontrar o penúltimo?
  • SÓ PERCORRENDO A LISTA INTEIRA do início!

Exemplo com [8, 4, 7, 2, 5]:
  • Queremos remover 5
  • Precisamos fazer 4.next = None e tail = 4
  • Mas começamos no head (8) e precisamos chegar até 4
  • Isso requer: 8 → 4 → 7 → 2 → 4 (parar aqui!)
  • Total: n-1 iterações = O(n)

COMPARAÇÃO COM OUTRAS ESTRUTURAS:
  • Deque com lista DUPLAMENTE encadeada: remove_end() = O(1)
    → Porque tail.prev já aponta direto para o penúltimo!
  
  • Deque com array circular: remove_end() = O(1)
    → Remove direto do índice final
"""
print(explicacao)
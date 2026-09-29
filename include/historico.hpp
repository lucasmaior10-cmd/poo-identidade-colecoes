#pragma once
#include "colecoes.hpp"
#include <vector>

// Histórico de UM sensor. Repetições são ocorrências, não duplicatas de cadastro.
class Historico {
    std::vector<Medicao> leituras_;
public:
    void registrar(const Medicao& leitura) { leituras_.push_back(leitura); }
    std::size_t quantidade() const { return leituras_.size(); }
    std::vector<Medicao> ultimas(std::size_t limite) const {
        if (limite == 0 || leituras_.empty()) {
            return std::vector<Medicao>();
        }
        
        std::size_t tamanho = leituras_.size();
        std::size_t qtd = (limite > tamanho) ? tamanho : limite;
        
        std::vector<Medicao> resultado;
        resultado.reserve(qtd);
        
        for (std::size_t i = tamanho - qtd; i < tamanho; ++i) {
            resultado.push_back(leituras_[i]);
        }
        
        return resultado;
    }
};

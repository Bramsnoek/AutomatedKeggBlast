from Models import Gene, PathwayEntry, Pathway
from typing import List, Dict, Any, TypeVar, Callable
import json
from Bio import TogoWS

T = TypeVar("T")

def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]

def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }

def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x

def genes_from_dict(s: Any) -> List[Dict[str, str]]:
    return from_list(lambda x: from_dict(from_str, x), s)

def genes_to_dict(x: List[Dict[str, str]]) -> Any:
    return from_list(lambda x: from_dict(from_str, x), x)


class KeggClient(object):
    def __init__(self, *organisms):
        self.__organisms = organisms

    def get_pathway(self, pathway_id):
        return Pathway(pathway_id, self.__get_genes_in_pathway_for_organisms(pathway_id))

    def __get_genes_in_pathway_for_organisms(self, pathway_id):
        entries = []
        gene_sets = genes_from_dict(json.loads(TogoWS.entry("pathway", ["{}{}".format(x, pathway_id) for x in self.__organisms], format="json", field="genes").read()))

        for i in range(0, len(gene_sets)):
            current_organism = self.__organisms[i]

            entries.append(PathwayEntry(current_organism, self.__get_nt_seq_for_genes(current_organism, gene_sets[i])))

        return entries

    @classmethod
    def __get_nt_seq_for_genes(cls, org, gene_dict):
        genes = []
        gene_seqs = json.loads(TogoWS.entry("genes", ["{}:{}".format(org, x) for x in list(gene_dict.keys())], format="json", field="ntseq").read())
        aa_seqs = json.loads(TogoWS.entry("genes", ["{}:{}".format(org, x) for x in list(gene_dict.keys())], format="json", field="aaseq").read())

        for i in range(0, len(gene_seqs)):
            gene_id = list(gene_dict.keys())[i]
            genes.append(Gene(gene_id, gene_dict[gene_id], gene_seqs[i], aa_seqs[i]))

        return genes
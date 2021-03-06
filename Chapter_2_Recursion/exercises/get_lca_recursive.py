import tax_dict as td

# uses list from tax_dict.py (global variable) 
tax_dict = td.tax_dict_1

def get_ancestors_rec(taxon):
	if taxon == 'Primates':
		return [taxon]
	else:
		parent = tax_dict.get(taxon)
		parent_ancestors = get_ancestors_rec(parent) 
		return [parent] + parent_ancestors
        
def get_lca(taxon1, taxon2): 
    taxon1_ancestors = [taxon1] + get_ancestors_rec(taxon1) 
    for taxon in [taxon2] + get_ancestors_rec(taxon2): 
        if taxon in taxon1_ancestors: 
            return taxon 

# shape the solution -- easier to read, but harder to code?
def get_lca_list_rec(taxa): 
    print("getting lca for " + str(taxa)) 
    if len(taxa) == 2: 
        return get_lca(taxa[0], taxa[1]) 
    else: 
        taxon1 = taxa.pop() 
        taxon2 = get_lca_list_rec(taxa) 
        return get_lca(taxon1, taxon2) 

print(get_lca_list_rec(['Pan troglodytes','Tarsius tarsier', 'Pongo abelii']))

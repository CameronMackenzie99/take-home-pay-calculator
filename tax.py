

def max_tax(tax_bands: list) -> list:
    """Returns a list of the maximum tax payable for each tax band."""
    print(tax_bands)
    segments = []
    for i, band in enumerate(tax_bands[1:], 1):
        segments.append(tax_bands[i]-tax_bands[i-1])
        print(segments)

tax_bands = [12570, 50270, 150000]
max_tax(tax_bands)

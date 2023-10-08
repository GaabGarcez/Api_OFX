def ofx_to_xml(ofx_content):
    # Dividir o conteúdo OFX em linhas
    lines = ofx_content.splitlines()

    # Encontrar a linha onde o XML começa (ignorando cabeçalhos OFX)
    for index, line in enumerate(lines):
        if line.strip().startswith("<OFX>"):
            break

    # Juntar as linhas a partir do ponto de início do XML
    xml_content = "\n".join(lines[index:])
    
    return xml_content

# Uso
ofx_content = """
OFXHEADER:100
DATA:OFXSGML
VERSION:102
SECURITY:NONE
ENCODING:USASCII
CHARSET:1252
COMPRESSION:NONE
OLDFILEUID:NONE
NEWFILEUID:NONE

<OFX>
  <SIGNONMSGSRSV1>
    <SONRS>
      <STATUS>
        <CODE>0
        <SEVERITY>INFO
      </STATUS>
      <DTSERVER>20220101120000
      <LANGUAGE>ENG
    </SONRS>
  </SIGNONMSGSRSV1>
</OFX>
"""

xml_content = ofx_to_xml(ofx_content)
print(xml_content)
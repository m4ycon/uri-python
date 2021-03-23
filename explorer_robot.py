def buscarArtefato():
  if bb8.verificarSeFoiVisitado():
    return
  bb8.registrarComoVisitado()

  if bb8.verificarChao():
    return bb8.verificarChao()
  
  caminhos_possiveis = [bb8.verificarNorte(), bb8.verificarSul(), bb8.verificarLeste(), bb8.verificarOeste()]
  mover = [bb8.moverNorte, bb8.moverSul, bb8.moverLeste, bb8.moverOeste]

  for i, caminho in enumerate(caminhos_possiveis):
    if caminho:
      mover[i]()
      res = buscarArtefato()
      if res != None:
        return res
      volta_i = 0 if i == 1 else (1 if i == 0 else (2 if i == 3 else 3))
      mover[volta_i]()

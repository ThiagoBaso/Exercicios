USE faculdade;
SHOW TABLES;

#1
SELECT a.nome AS aluno, c.nome AS curso
FROM alunos a
INNER JOIN cursos c
ON a.curso_id = c.id
WHERE c.nome = 'Análise e Desenvolvimento de Sistemas'
ORDER BY a.nome ASC;

#2
SELECT d.nome AS disciplina, p.nome AS professor
FROM disciplinas d 
INNER JOIN professores p
ON d.professor_id = p.id;

#3
SELECT * FROM disciplinas
WHERE professor_id IS NULL;

#4
SELECT * FROM professores p
INNER JOIN disciplinas d;
SELECT alunos.nome, cursos.nome FROM alunos
INNER JOIN cursos ON alunos.curso_id = cursos.id;

SELECT a.nome, c.nome
FROM alunos a
INNER JOIN cursos c ON a.curso_id = c.id
WHERE c.nome = 'Engenharia de Software'
ORDER BY a.nome DESC;

SELECT d.nome AS Disciplina, p.nome AS Professor
FROM disciplinas d
LEFT JOIN professores p ON d.professor_id = p.id;

SELECT *
FROM professores p
LEFT JOIN disciplinas d ON p.id = d.professor_id
WHERE d.id IS NULL;

SELECT p.nome
FROM disciplinas d
RIGHT JOIN professores p ON p.id = d.professor_id;

SELECT c.nome, a.nome
FROM cursos c
INNER JOIN alunos a ON c.id = a.curso_id;

SELECT c.nome, COUNT(*), COUNT(a.id)
FROM cursos c
INNER JOIN alunos a ON c.id = a.curso_id
GROUP BY c.nome;

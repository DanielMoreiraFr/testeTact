 const getD = (id) => {

    const element = document.getElementById(id);

    if (!element) {

        console.warn(`Elemento com ID ${id} não encontrado.`);

        return [];

    }

    try {

        return JSON.parse(element.textContent);

    } catch (e) {

        console.error(`Erro ao analisar JSON do ID ${id}:`, e);

        return [];

    }

};


const optionsPadrao = {

    responsive: true,

    maintainAspectRatio: false,

    scales: {

        y: {

            min: 0, /* menor valor possível */

            max: 100, /* maior valor */

            ticks: { stepSize: 20 }

        }

    }

};


document.addEventListener('DOMContentLoaded', () => {

   

    // 1. Gênero (Barra)

    new Chart(document.getElementById('chartGenero'), {

        type: 'bar',

        data: {

            labels: getD('l-gen'),

            datasets: [{ label: 'Nota',

                data: getD('d-gen'),

                backgroundColor: [

                    '#e69703',

                ] }]

        },

        options: optionsPadrao

    });


    // 2. Ansiedade (Barra)

    new Chart(document.getElementById('chartAnsiedade'), {

        type: 'bar',

        data: {

            labels: getD('l-ans'),

            datasets: [{

                label: 'Nota',

                data: getD('d-ans'),

                backgroundColor: [

                    '#e74a3b',

                ] }]

        },

        options: optionsPadrao

    });


    // 3. Pizza: Faixa Etária

    new Chart(document.getElementById('chartIdade'), {

        type: 'pie',

        data: {

            labels: getD('l-idade'),

            datasets: [{

                data: getD('d-idade'),

                backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b']

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: { legend: { position: 'bottom' } }

        }

    });


    // 4. Renda (Barra)

    new Chart(document.getElementById('chartRenda'), {

        type: 'bar',

        data: {

            labels: getD('l-renda'),

            datasets: [{ label: 'Nota', data: getD('d-renda'), backgroundColor: '#1cc88a' }]

        },

        options: optionsPadrao

    });


    // 5. Sono (Linha)

    new Chart(document.getElementById('chartSono'), {

        type: 'line',

        data: {

            labels: getD('l-sono'),

            datasets: [{ label: 'Nota',

                data: getD('d-sono'),

                borderColor: '#4e73df',

                backgroundColor: 'rgba(78, 115, 223, 0.1)',

                fill: true,

                tension: 0.3 }]

        },

        options: optionsPadrao

    });


    // 6. Tela (Linha)

    new Chart(document.getElementById('chartTela'), {

        type: 'line',

        data: {

            labels: getD('l-tela'),

            datasets: [{ label: 'Nota',

                    data: getD('d-tela'),

                    borderColor: '#f6c23e',

                    backgroundColor: 'rgba(246, 194, 62, 0.1)',

                    fill: true,

                    tension: 0.3 }]

        },

        options: optionsPadrao

    });


    // 7. Frequência (Linha com preenchimento)

    new Chart(document.getElementById('chartFreq'), {

        type: 'line',

        data: {

            labels: getD('l-freq'),

            datasets: [{

                label: 'Nota Final',

                data: getD('d-freq'),

                borderColor: '#198754',

                fill: true,

                backgroundColor: 'rgba(25,135,84,0.1)',

                tension: 0.4

            }]

        },

        options: optionsPadrao

    });


    // 8. Ansiedade por tempo de sono (Tendência)

    new Chart(document.getElementById('chartSonoAnsiedade'), {

        type: 'line',

        data: {

            labels: getD('l-sono-ans'),

            datasets: [{

                label: 'Nível Médio de Ansiedade',

                data: getD('d-sono-ans'),

                borderColor: '#58016c',

                backgroundColor: 'rgba(73, 4, 138, 0.2)',

                fill: true,

                tension: 0.3

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            scales: {

                y: {

                    beginAtZero: true,

                    title: { display: true, text: 'Nível de Ansiedade' }

                },

                x: {

                    title: { display: true, text: 'Horas de Sono' }

                }

            }

        }

    });


    // 9. Trabalho vs Desempenho --> usa da API REST do app api

    fetch('/api/dashboard/stats/')

        .then(response => response.json())

        .then(res => {

            const dadosTrabalho = res.trabalho_vs_desempenho; // pegando a key definida no api/view.py


        new Chart(document.getElementById('chartTrabalho'), {

            type: 'bar',

            data: {

                labels: dadosTrabalho.l_trabalho_nota,

                datasets: [{

                    label: 'Média da Nota Final',

                    data: dadosTrabalho.d_trabalho_nota,

                    backgroundColor: [

                        '#4edf53', // Trabalha

                        '#c81c1c'  // Não Trabalha

                    ],

                    borderWidth: 1

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                scales: {

                    y: {

                        beginAtZero: true,

                        max: 100,

                        title: { display: true, text: 'Média de Pontos' }

                    }

                },

                plugins: {

                    legend: { display: false }

                }

            }

        });

    })

    .catch(error => console.error('Erro ao buscar dados da API:', error));

}); 
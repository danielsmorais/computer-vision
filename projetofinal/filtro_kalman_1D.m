opengl('save','hardware')

%Filtra os dados do GPS 1D
% Armazena a pasta atual
OLDDIR=pwd();
% Pasta de leitura dos arquivos
DATADIR='/home/daniel/Git/computer-vision/projetofinal';
%DATADIR='C:\Users\Daniel Morais\Documents\git\system-identification\Projeto_2';
if (~chdir(DATADIR))
    error('Folder does not exist');
end

% Arquivo com as medicoes
FILE='dados.txt';
% Leitura dos dados
% 2 colunas = x y
data = dlmread(FILE);
npassos = size(data,1);

dt = 1/30;

% Vetor de estados
% X = [x,y,vx,vy]
X = [546;223;0;0];
% Matriz de transicao
% Xk+1 = PHI*Xk + u
PHI = [1 0 dt 0;
       0 1 0 dt;
       0 0 1 0;
       0 0 0 1];
% Variancia da estimativa
% Inicialmente nula pois a condicao inicial eh conhecida
P = [0 0 0 0;
     0 0 0 0;
     0 0 0 0;
     0 0 0 0];

 % Variancia do ruido dinamico
Q = [1.5^2 0 0 0; 
     0 1.5^2 0 0;
     0 0 1.5^2 0;
     0 0 0 1.5^2]*60;

% Matriz de medicao
H = [1 0 0 0;
     0 1 0 0];
% Variancia do ruido de medicao
R = [133^2 0;
     0 75^2]*0.05;

% Dados filtrados
% 4 colunas = x y vx vy
filtr = zeros(npassos,4);


% Filtragem
for (i=1:npassos)
    % Fase de predicao
    X = PHI*X;
    P = PHI*P*PHI' + Q;
    
    % Medicao
    Y = [data(i,1); data(i,2)];
    
    % Fase de correcao
    K = P*H'*inv(H*P*H'+R);
    X = X + K*(Y-H*X);
    P = P - K*H*P;
    
    % salva os pontos
    filtr(i,1) = X(1,1);
    filtr(i,2) = X(2,1);
    filtr(i,3) = X(3,1);    
    filtr(i,4) = X(4,1);  
end

% Percurso xy
figure(1)
plot(filtr(:,1), filtr(:,2), 'b', data(:,1), data(:,2), '.r');

% Evolucao de x
% plot(real(:,1), real(:,2), 'kx', data(:,1), filtr(:,1), '-b', data(:,1), data(:,2), 'ro');
% Evolucao de y
% plot(real(:,1), real(:,3), 'kx', data(:,1), filtr(:,2), '-b', data(:,1), data(:,3), 'ro');
% Evolucao de v
% plot(real(:,1), real(:,4), 'kx', data(:,1), filtr(:,3), '-b');

% Volta para a pasta anterior
chdir(OLDDIR);

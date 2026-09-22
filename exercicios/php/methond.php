<?php 

    abstract class Pagamento {
        public function processarPagamento() {
            $this->validarDados();
            $this->conectarAoGateway();
            $this->autorizarPagamento();
            $this->confirmarPagamento();
        }

        abstract protected function validarDados();
        abstract protected function conectarAoGateway();
        abstract protected function autorizarPagamento();

        protected function COnfirmarPagamento() {
            echo "Pagamento confirmado.\n";
        }
    }

    class PagamentoCartaoCredito extends Pagamento {
        
        protected function validarDados()
        {
            echo "validando dados...";
        }

        protected function conectarAoGateway()
        {
            echo "conectando ao ga...";
        }

        
        protected function autorizarPagamento()
        {
            echo "autorizando pagamento...";  
        }
    }

    class PAgamentoPayPal extends Pagamento {
        protected function validarDados()
            {
                echo "validando dados...";
            }

            protected function conectarAoGateway()
            {
                echo "conectando ao ga...";
            }

            
            protected function autorizarPagamento()
            {
                echo "autorizando pagamento...";  
            }
    }


    $pagamentoCartao = new PagamentoCartaoCredito();
    $pagamentoCartao-> processarPagamento();

    $pagamentoPayPal = new PAgamentoPayPal();
    $pagamentoPayPal->processarPagamento();

?>
<?php 

    abstract class Pedido {
        abstract function adicionarProduto();
        abstract function calcularTotal();
    }

    interface Notificavel
    {
        public function enviarNotificacao($mensagem);
    }

    class PedidoComum extends Pedido {

        function adicionarProduto()
        {
            
        }

        function calcularTotal()
        {
            
        }
    }

    class PedidoExpresso extends Pedido {

        function adicionarProduto()
        {
            
        }

        function calcularTotal()
        {
            
        }
    }

    class Email implements Notificavel
    {
        public function enviarNotificacao($mensagem)
        {
            echo "Email: $mensagem\n";
        }
    }

    class SMS implements Notificavel
    {
        public function enviarNotificacao($mensagem)
        {
            echo "SMS: $mensagem\n";
        }
    }
?>
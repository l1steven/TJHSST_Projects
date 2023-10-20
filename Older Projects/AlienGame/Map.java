import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.io.*;
public class Map extends JPanel implements ActionListener
{
   private Character c;
   private ArrayList<Enemy> bots;
   private int numOfEnemy;
   private int level;
   private int score;
   private boolean gameOn;
   public static enum GameState { MENU,GAME,DEAD } ;
   private static GameState state;
   private Scoreboard board;
   private Menu menu;
   public static final int SIDE=800;
   public static final int BOTTOM=700;
   private Timer timer;
   private JButton button;
   private JButton button2;
   public Map()
   {
     state=GameState.MENU;
     addMouseListener(new Listener2());
     setFocusable(true);
     addKeyListener(new Listener());
     setFocusable(true);
     
     setBackground(Color.BLACK);
   
     setSize(SIDE,BOTTOM);
     setLayout(null);
     button=new JButton("New Game");
     button.setBounds(330,600,140,20);
     button.addActionListener(new ResetListener());
     add(button);
     button2=new JButton("Return to Menu");
     button2.setBounds(330,620,140,20);
     button2.addActionListener(new MenuListener());
     add(button2);
     board=new Scoreboard();
     board.setBounds(0,600,800,100);
     add(board);
      gameOn=true;
     c=new Character("duck_30x30.png");
     bots=new ArrayList<Enemy>();
     numOfEnemy=5;
     for(int x=0;x<numOfEnemy;x++)
     {
      bots.add(new Enemy("alien30.png"));
     }
     menu=new Menu();
     timer = new Timer(5, this);
     timer.start();
   }
   public static void setState(GameState g)
   {
      state=g;
   }
   public static GameState getState()
   {
      return state;
   }
   public void paintComponent(Graphics g)
   {
      super.paintComponent(g);
      if(state==GameState.GAME)
      {
         g.drawImage(c.getImage(), c.getX(), c.getY(), null);  //draw all entities
         for(Enemy e: bots)
         {
            g.drawImage(e.getImage(), e.getX(), e.getY(), null);
            for(Bullet b:e.getBullets())
            {
               g.drawImage(b.getImage(), b.getX(), b.getY(), null);
            }
         }
         for(Bullet b:c.getBullets())
         {
            g.setColor(Color.WHITE);
            //g.drawImage(b.getImage(), b.getX(),b.getY(),null);
            g.fillOval(b.getX(),b.getY(),6,6);
         }
         g.setFont(new Font("Serif",Font.BOLD,20));
         g.setColor(Color.WHITE);
         g.drawString("HP: " + c.getHP(),700,600);
         g.drawString("Level: "+level+1,700,640);   //draw hp and score
        // g.drawString("Score: " +score, 50,600);
         board.paintComponent(g);
      }
      if(state==GameState.MENU)
      {
         menu.drawButtons(g);
      }
      
   }
   
   public void actionPerformed(ActionEvent e)
   {
      if(gameOn)  //when character dies, game off
      {
         updateLevel();
         updateCharacter();
         updateAlien();                       //repeats with timer
         updateBullets();
         board.updateScore();
         repaint();
      }
      if(state==GameState.MENU)
      {
         repaint();
      }
   }
   
   private class ResetListener implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {
         numOfEnemy=5;
         bots.clear();
         for(int x=0;x<5;x++)
         {
            bots.add(new Enemy("alien30.png"));
         }
         level=1;
         c.setHP(3);
         score=0;
         gameOn=true;
         button.setFocusable(false);
         button2.setFocusable(false);
      }
   }
   private class MenuListener implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {  
         
         state=GameState.MENU;
         button.setFocusable(false);
         button2.setFocusable(false);
         if(c.getHP()==0)
         {
             c.setHP(3);
             numOfEnemy=5;
             bots.clear();
             for(int x=0;x<5;x++)
             {
                bots.add(new Enemy("alien30.png"));
             }
             level=1;
             c.setHP(3);
             score=0;
         }
         
      }
   }
   
   private class Listener extends KeyAdapter //for movement of character
   {
      public void keyPressed(KeyEvent e) 
      {
         if(gameOn)
         {
              int key = e.getKeyCode();
              if (key == KeyEvent.VK_A) 
              {
                  c.setdx(-1);
              }
      
              if (key == KeyEvent.VK_D) 
              {
                  c.setdx(1);
              }
      
              if (key == KeyEvent.VK_W) 
              {
                  c.setdy(-1);
              }
      
              if (key == KeyEvent.VK_S) 
              {
                  c.setdy(1);
              }
         }
      }
      public void keyReleased(KeyEvent e) 
      {
         if(gameOn)
         {
         
           int key = e.getKeyCode();
           if (key == KeyEvent.VK_A) 
           {
               c.setdx(0);
           }
   
           if (key == KeyEvent.VK_D) 
           {
               c.setdx(0);
           }
   
           if (key == KeyEvent.VK_W) 
           {
               c.setdy(0);
           }
   
           if (key == KeyEvent.VK_S) 
           {
              c.setdy(0);
           }
         }
      }
   }
   private class Listener2 extends MouseAdapter //shoots a bullet by the character
   {
      public void mousePressed(MouseEvent e)
      {
         int xl=e.getX()-c.getX()+15;
         int yl=e.getY()-c.getY()+15;
         double angle=(Math.atan2(yl,xl)*180/Math.PI);//////
         c.shoot(4,angle/*,e.getX(),e.getY()*/);
         score=score-1;
       //////////  
         if(Map.getState()==GameState.MENU)
         {
            int x=e.getX();
            int y=e.getY();
            if(x>Map.SIDE/2-50 && x<Map.SIDE/2+50)
            {
               if( y>Map.BOTTOM/2-25 && y<Map.BOTTOM/2+25)
               {
                  Map.setState(GameState.GAME);
                  gameOn=true;
               }
               
               if( y>Map.BOTTOM/2-125&& y<Map.BOTTOM/2-75)
               {
               //   try
                // {
                     /*ProcessBuilder p=new ProcessBuilder("Notepad.exe","scores.txt");
                     p.start();*/
                    menu.getCredits();
                //  }
               //   catch(IOException i)
              //    {
                //     JOptionPane.showMessageDialog(null, "Could not open file");
              //    }
               }
               if(y>Map.BOTTOM/2-225 && y<Map.BOTTOM/2-175)
               {
                  System.exit(0);
               }
            }
         
                  
               
            
         }
         
///////////////////////////////
      }
   }
   private void updateBullets()
   {
      ArrayList<Bullet> array= c.getBullets();        /////////////////////////////
      for(int x=0;x<array.size();x++)
      {
         Bullet temp = array.get(x);        
         temp.move();
         temp.detect();
         for(Enemy bot:bots)
         {
            if(temp.getBox().intersects(bot.getBox()))
            {
              temp.setVisible(false);                                //if character's bullets hit enemy
              bot.setHP(bot.getHP()-1);
              score=score+10;        //increase the score
            }    
         }
             
         if(!temp.isVisible)
         {
            array.remove(x);
         }
      }                                              //////////////////////
      
      
      
      for(Enemy bot:bots)                                            ///////////////////////////
      {
         ArrayList<Bullet> a=bot.getBullets();
         for(int x=0;x<a.size();x++)
         {
            Bullet temp=a.get(x);
            temp.move();
            temp.detect();
            
            if(temp.getBox().intersects(c.getBox()))                         //if enemy bullets hit character
            {
               temp.setVisible(false);
               c.setHP(c.getHP()-1);
            }
            if(!temp.getVisible())
            {
               a.remove(x);
            }
         }
      }                                                                        ///////////////////////////
      
   } 
   private void updateAlien()
   {
      
      for(Enemy e: bots)           //sets the level for the enemies
      {
         e.setLevel(level); 
      }
      for(int x=0;x<bots.size();x++)
      {
         Enemy temp=bots.get(x);           //set visible false if hp is less than 0
         if(temp.getHP()<=0)
         {
            temp.setVisible(false);
         }
         
         if(temp.getVisible())
         {
            temp.move(SIDE,BOTTOM);
            int random=(int)(Math.random()*300);  //move and shoot if visible
            if(random==0)
            {
               temp.shoot();
            }
         }
         else
         {
            bots.remove(x);                    //remove if false
            score=score+40;          //increase score
         }
      }
   }
   private void updateCharacter()
   {
      c.move(SIDE,BOTTOM);
      if(c.getHP()==0)                         //move, end game if hp=0
      {
         gameOn=false;
       //  try
       //  {
            board.save();
         //}
        
      }
   }
   private void updateLevel()
   {
      int remain=bots.size();
      boolean life=c.getVisible();
      if(remain==0)                                       //if no enemies left, level increase and more enemies
      {
         level++;
         score=score+500;    //increase score
         numOfEnemy=numOfEnemy+2;
         for(int x=0;x<numOfEnemy;x++)
         {
            bots.add(new Enemy("alien30.png"));
         }
         
      }
      board.setScore(score);
      
   }
   public int getScore()
   {
      return score;
   }

      
   
         
      
      
           
}
   
  
   
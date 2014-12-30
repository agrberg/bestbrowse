class AddEmailBrowserIdAndBrowserTypeToVisits < ActiveRecord::Migration
  def change
    add_column :visits, :email, :string
    add_column :visits, :browser_type, :string
    add_column :visits, :browser_id, :string

    add_index :visits, :email
    add_index :visits, [:browser_type, :browser_id]
  end
end
